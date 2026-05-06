import argparse
import logging
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

from .dedupe import canonical_id, dedupe
from .fetchers import arxiv_fetcher, github_trending, hn_newest, html, rss
from .models import Item
from .render import render_report
from .state import State


_SECTION_TO_CATEGORY = {
    "公司动态": "company",
    "个人 Blog": "individual",
    "社区动态": "community",
    "新论文 — 关注作者": "arxiv-author",
    "新论文 — 关键词命中": "arxiv-keyword",
}
_BULLET_RE = re.compile(r"^- (?:\*\*([^*]+)\*\* — )?\[(.+?)\]\(([^)]+)\)")


def _parse_existing_report(path: Path) -> list[Item]:
    items: list[Item] = []
    section = ""
    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        m = _BULLET_RE.match(line)
        if not m:
            continue
        category = _SECTION_TO_CATEGORY.get(section)
        if not category:
            continue
        source = m.group(1) or ("arXiv (keyword)" if category == "arxiv-keyword" else section)
        url = m.group(3)
        items.append(Item(
            id=canonical_id(url),
            title=m.group(2),
            url=url,
            source=source,
            category=category,
        ))
    return items


ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "config" / "sources.yaml"
TEMPLATES = ROOT / "templates"
DATA_DIR = ROOT / "data"
REPORTS_DIR = ROOT / "reports"
LOGS_DIR = ROOT / "logs"


def _setup_logging() -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(LOGS_DIR / "aidigest.log"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def _load_config() -> dict:
    with CONFIG.open() as f:
        return yaml.safe_load(f)


def _collect_all(cfg: dict) -> tuple[list[Item], list[str]]:
    items: list[Item] = []
    errors: list[str] = []
    rss_lookback = cfg.get("rss_lookback_days")

    for src in cfg.get("companies", []):
        try:
            if src["type"] == "rss":
                items.extend(rss.fetch(src["name"], src["url"], "company", rss_lookback))
            elif src["type"] == "html":
                items.extend(
                    html.fetch(src["name"], src["url"], src["link_pattern"], "company")
                )
        except Exception as e:
            logging.exception("company source %s failed", src["name"])
            errors.append(f"{src['name']}: {e}")

    for src in cfg.get("individuals", []):
        try:
            if src["type"] == "rss":
                items.extend(rss.fetch(src["name"], src["url"], "individual", rss_lookback))
            elif src["type"] == "html":
                items.extend(
                    html.fetch(src["name"], src["url"], src["link_pattern"], "individual")
                )
        except Exception as e:
            logging.exception("individual source %s failed", src["name"])
            errors.append(f"{src['name']}: {e}")

    for src in cfg.get("community", []):
        try:
            if src["type"] == "github_trending":
                items.extend(github_trending.fetch(src["name"], src["url"]))
            elif src["type"] == "hn_newest":
                items.extend(hn_newest.fetch(src["name"], src["url"]))
        except Exception as e:
            logging.exception("community source %s failed", src["name"])
            errors.append(f"{src['name']}: {e}")

    arx = cfg.get("arxiv", {})
    if arx:
        try:
            items.extend(
                arxiv_fetcher.fetch_by_keywords(
                    categories=arx["categories"],
                    keywords=arx["keywords"],
                    max_results=arx["max_results_per_query"],
                    lookback_days=arx["lookback_days"],
                )
            )
        except Exception as e:
            logging.exception("arxiv keyword search failed")
            errors.append(f"arXiv keywords: {e}")

        try:
            items.extend(
                arxiv_fetcher.fetch_by_authors(
                    authors=arx["authors"],
                    max_results_per_author=arx["max_results_per_query"],
                    lookback_days=arx["lookback_days"],
                )
            )
        except Exception as e:
            logging.exception("arxiv author search failed")
            errors.append(f"arXiv authors: {e}")

    return dedupe(items), errors


def cmd_init(args: argparse.Namespace) -> int:
    cfg = _load_config()
    items, errors = _collect_all(cfg)
    state = State(DATA_DIR / "seen.sqlite")
    state.mark_many([(i.id, i.source) for i in items])
    print(f"Seeded {len(items)} items into seen DB ({state.count()} total).")
    if errors:
        print(f"Errors: {errors}")
    state.close()
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    cfg = _load_config()
    items, errors = _collect_all(cfg)
    state = State(DATA_DIR / "seen.sqlite")

    new_items = [i for i in items if not state.is_seen(i.id)]
    state.mark_many([(i.id, i.source) for i in new_items])
    state.close()

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.md"

    # Merge with today's existing report so a same-day re-run doesn't drop entries
    # that were already written but are now in the seen DB. Today's items =
    # previously rendered ∪ new in this run. Prefer fresh fetched data (published,
    # authors) over the re-parsed sparse version when both are available.
    existing = _parse_existing_report(out) if out.exists() else []
    fresh_by_url = {it.url: it for it in items}
    today_urls = {it.url for it in existing} | {it.url for it in new_items}
    parsed_by_url = {it.url: it for it in existing}
    merged_items = [fresh_by_url.get(url) or parsed_by_url[url] for url in today_urls]

    body = render_report(merged_items, TEMPLATES, errors)
    out.write_text(body)
    print(
        f"Wrote {out} ({len(new_items)} new items, {len(merged_items)} total, "
        f"{len(errors)} errors)"
    )
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    cfg = _load_config()
    rss_lookback = cfg.get("rss_lookback_days")
    bad = 0
    for group in ("companies", "individuals"):
        for src in cfg.get(group, []):
            try:
                if src["type"] == "rss":
                    found = len(rss.fetch(src["name"], src["url"], group, rss_lookback))
                else:
                    found = len(
                        html.fetch(src["name"], src["url"], src["link_pattern"], group)
                    )
                status = "OK " if found else "EMPTY"
                if not found:
                    bad += 1
                print(f"  {status} {src['name']:25s} {found:>3} items  {src['url']}")
            except Exception as e:
                bad += 1
                print(f"  FAIL {src['name']:25s} {e}")
    for src in cfg.get("community", []):
        try:
            if src["type"] == "github_trending":
                found = len(github_trending.fetch(src["name"], src["url"]))
            elif src["type"] == "hn_newest":
                found = len(hn_newest.fetch(src["name"], src["url"]))
            else:
                found = 0
            status = "OK " if found else "EMPTY"
            if not found:
                bad += 1
            print(f"  {status} {src['name']:25s} {found:>3} items  {src['url']}")
        except Exception as e:
            bad += 1
            print(f"  FAIL {src['name']:25s} {e}")
    return 1 if bad else 0


def main() -> int:
    _setup_logging()
    parser = argparse.ArgumentParser(prog="aidigest")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="Seed seen DB with current items (no report)")
    sub.add_parser("run", help="Fetch new items and write today's report")
    sub.add_parser("verify", help="Check that all sources return items")
    args = parser.parse_args()
    return {"init": cmd_init, "run": cmd_run, "verify": cmd_verify}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
