import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

import yaml

from .dedupe import dedupe
from .fetchers import arxiv_fetcher, html, rss
from .models import Item
from .render import render_report
from .state import State


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

    body = render_report(new_items, TEMPLATES, errors)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.md"
    out.write_text(body)
    print(f"Wrote {out} ({len(new_items)} new items, {len(errors)} errors)")
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
