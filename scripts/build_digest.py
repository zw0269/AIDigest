"""扫 reports/*.md，按日期生成 llm-ai/digests/digest-{date}.{md,html}。

输出：
- llm-ai/digests/digest-{date}.md  — 中间产物，方便检查
- llm-ai/digests/digest-{date}.html — 双语 Notion 风格

用法：
    build_digest.py [<date>]      # 不带参数 = 全部 reports
"""

import re
import sys
from html import escape, unescape
from pathlib import Path

import feedparser
import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.data import MANUAL_SUMMARIES, TRANSLATIONS  # noqa: E402


REPORTS = ROOT / "reports"
CONFIG = ROOT / "config" / "sources.yaml"
DIGESTS = ROOT / "llm-ai" / "digests"


CSS = """
:root {
  --bg: #ffffff;
  --bg-warm: #f6f5f4;
  --text: rgba(0,0,0,0.95);
  --text-muted: #615d59;
  --text-dim: #a39e98;
  --blue: #0075de;
  --blue-active: #005bab;
  --focus: #097fe8;
  --badge-bg: #f2f9ff;
  --badge-text: #097fe8;
  --whisper: 1px solid rgba(0,0,0,0.1);
  --shadow-card: rgba(0,0,0,0.04) 0 4px 18px,
                 rgba(0,0,0,0.027) 0 2.025px 7.84688px,
                 rgba(0,0,0,0.02) 0 0.8px 2.925px,
                 rgba(0,0,0,0.01) 0 0.175px 1.04062px;
  --font: "NotionInter", Inter, -apple-system, system-ui, "Segoe UI", Helvetica,
          "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--font); font-size: 16px; line-height: 1.5;
  color: var(--text); background: var(--bg);
  font-feature-settings: "lnum", "locl";
  -webkit-font-smoothing: antialiased;
}
a { color: var(--blue); text-decoration: none; }
a:hover { text-decoration: underline; }
a:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; border-radius: 4px; }

.container { max-width: 1080px; margin: 0 auto; padding: 0 24px; }

.topnav {
  padding: 20px 24px; border-bottom: var(--whisper);
  display: flex; justify-content: space-between; align-items: center;
  font-size: 14px; font-weight: 500;
}
.topnav a.back {
  color: var(--text-muted);
  display: inline-flex; align-items: center; gap: 6px;
}
.topnav a.back:hover { color: var(--blue); }

.hero { padding: 80px 24px 56px; text-align: center; background: var(--bg); }
.hero-eyebrow {
  display: inline-block; padding: 4px 10px;
  background: var(--badge-bg); color: var(--badge-text);
  border-radius: 9999px; font-size: 12px; font-weight: 600;
  letter-spacing: 0.125px; margin-bottom: 24px;
}
.hero h1 {
  font-size: 64px; font-weight: 700; line-height: 1.0;
  letter-spacing: -2.125px; color: var(--text); margin-bottom: 16px;
}
.hero p.lead {
  font-size: 18px; font-weight: 400; line-height: 1.4;
  color: var(--text-muted); max-width: 720px; margin: 0 auto 36px;
}
.hero-meta { display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; }
.metric {
  background: var(--bg); border: var(--whisper); border-radius: 12px;
  padding: 14px 22px; min-width: 120px; box-shadow: var(--shadow-card);
}
.metric-value {
  font-size: 28px; font-weight: 700; line-height: 1.0;
  letter-spacing: -0.5px; color: var(--text);
}
.metric-label {
  font-size: 12px; font-weight: 500; color: var(--text-muted);
  margin-top: 6px; letter-spacing: 0.125px;
}

section.section { padding: 72px 0; }
section.section.alt { background: var(--bg-warm); }
section.section h2 {
  font-size: 44px; font-weight: 700; line-height: 1.0;
  letter-spacing: -1.4px; color: var(--text); margin-bottom: 10px;
}
section.section .section-meta {
  font-size: 14px; font-weight: 500; color: var(--text-muted); margin-bottom: 40px;
}

.source-group { margin-bottom: 48px; }
.source-group:last-child { margin-bottom: 0; }
.source-header {
  display: flex; align-items: baseline; justify-content: space-between;
  gap: 16px; margin-bottom: 18px; padding-bottom: 12px; border-bottom: var(--whisper);
}
.source-name {
  font-size: 24px; font-weight: 700; line-height: 1.23;
  letter-spacing: -0.5px; color: var(--text);
}
.source-count {
  font-size: 12px; font-weight: 600; letter-spacing: 0.125px;
  color: var(--badge-text); background: var(--badge-bg);
  padding: 4px 8px; border-radius: 9999px;
}

.item {
  background: var(--bg); border: var(--whisper); border-radius: 12px;
  padding: 18px 22px; margin-bottom: 12px; transition: box-shadow 0.15s ease;
}
.item:hover { box-shadow: var(--shadow-card); }
section.alt .item { background: var(--bg); }
.item-title {
  font-size: 19px; font-weight: 600; line-height: 1.4;
  letter-spacing: -0.125px; color: var(--text);
  display: block; margin-bottom: 10px;
}
.item-title:hover { color: var(--blue); text-decoration: none; }
.item-summary {
  font-size: 15px; font-weight: 400; line-height: 1.55;
  color: var(--text-muted); margin-bottom: 6px;
}
.item-summary:last-child { margin-bottom: 0; }
.item-summary.zh {
  color: var(--text); font-size: 15px;
  padding-top: 8px; margin-top: 8px;
  border-top: 1px dashed rgba(0,0,0,0.07);
}
.item-summary .lang-tag {
  display: inline-block; font-size: 10px; font-weight: 600;
  color: var(--text-dim); letter-spacing: 0.5px;
  margin-right: 8px; padding: 1px 5px; border-radius: 3px;
  background: var(--bg-warm); vertical-align: 2px;
}
.item-url {
  display: block; font-size: 12px; font-weight: 500;
  color: var(--text-dim); letter-spacing: 0.125px;
  margin-top: 10px; word-break: break-all;
}

footer {
  padding: 48px 24px 64px; border-top: var(--whisper);
  text-align: center; color: var(--text-muted); font-size: 14px;
}

@media (max-width: 768px) {
  .hero { padding: 56px 24px 40px; }
  .hero h1 { font-size: 38px; letter-spacing: -1.2px; }
  section.section { padding: 56px 0; }
  section.section h2 { font-size: 30px; letter-spacing: -0.9px; }
  .source-name { font-size: 20px; }
  .item { padding: 14px 16px; }
  .item-title { font-size: 16px; }
}
"""


# ---- parse ----

def parse_report(p: Path) -> list[dict]:
    items = []
    section = ""
    line_re = re.compile(r"^- (?:\*\*([^*]+)\*\* — )?\[([^\]]+)\]\(([^)]+)\)")
    for line in p.read_text().splitlines():
        line = line.strip()
        if line.startswith("## "):
            section = line[3:].strip()
        m = line_re.match(line)
        if m:
            items.append({
                "section": section,
                "source": m.group(1) or section,
                "title": m.group(2),
                "url": m.group(3),
            })
    return items


def strip_html(text: str) -> str:
    return unescape(re.sub(r"<[^>]+>", "", text or "")).strip()


_RSS_INDEX_CACHE: dict[str, str] | None = None


def rss_index() -> dict[str, str]:
    global _RSS_INDEX_CACHE
    if _RSS_INDEX_CACHE is not None:
        return _RSS_INDEX_CACHE
    cfg = yaml.safe_load(CONFIG.read_text())
    index: dict[str, str] = {}
    for group in ("companies", "individuals"):
        for src in cfg.get(group, []):
            if src.get("type") != "rss":
                continue
            f = feedparser.parse(src["url"])
            for e in f.entries:
                link = getattr(e, "link", None)
                if not link:
                    continue
                desc = getattr(e, "description", "") or getattr(e, "summary", "")
                desc = strip_html(desc)
                if len(desc) > 350:
                    desc = desc[:347] + "..."
                index[link.rstrip("/")] = desc
    _RSS_INDEX_CACHE = index
    return index


def enrich(items: list[dict]) -> list[dict]:
    """Add 'en' (RSS desc) and 'zh' (translation/manual) fields."""
    rss = rss_index()
    out = []
    for it in items:
        u = it["url"]
        u_norm = u.rstrip("/")
        en, zh = "", ""
        if u in MANUAL_SUMMARIES:
            zh = MANUAL_SUMMARIES[u]
        else:
            en = rss.get(u_norm, "")
            zh = TRANSLATIONS.get(u, "")
        out.append({**it, "en": en, "zh": zh})
    return out


# ---- md output ----

def render_md(date: str, items: list[dict]) -> str:
    lines = [f"# AIDigest 内容摘要 — {date}\n"]
    lines.append(f"对当日抓取的 **{len(items)} 条** 内容逐一阅读，给出一句话核心要点。\n")

    by_section: dict[str, list[dict]] = {}
    for it in items:
        by_section.setdefault(it["section"], []).append(it)

    for section in ("公司动态", "个人 Blog", "新论文 — 关注作者", "新论文 — 关键词命中"):
        group = by_section.get(section)
        if not group:
            continue
        lines.append(f"\n## {section}（{len(group)} 条）\n")
        by_source: dict[str, list[dict]] = {}
        for it in group:
            by_source.setdefault(it["source"], []).append(it)
        for source, sg in by_source.items():
            lines.append(f"\n### {source}\n")
            for it in sg:
                lines.append(f"- **[{it['title']}]({it['url']})**")
                if it["en"]:
                    lines.append(f"  - EN: {it['en']}")
                if it["zh"]:
                    lines.append(f"  - 中文: {it['zh']}")
    return "\n".join(lines) + "\n"


# ---- html output ----

def slugify(s: str) -> str:
    s = re.sub(r"[^\w一-鿿]+", "-", s).strip("-").lower()
    return s or "section"


def render_html(date: str, items: list[dict]) -> str:
    by_section: dict[str, list[dict]] = {}
    for it in items:
        by_section.setdefault(it["section"], []).append(it)

    total = len(items)
    by_section_count = {k: len(v) for k, v in by_section.items()}
    sources_set = {it["source"] for it in items}

    parts: list[str] = []
    parts.append(f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AIDigest — {date}</title>
<style>{CSS}</style>
</head>
<body>

<nav class="topnav">
  <div><a href="../index.html" class="back">← 返回首页</a></div>
  <div style="color:var(--text-muted)">AIDigest · {date}</div>
</nav>

<div class="hero">
  <span class="hero-eyebrow">{date}</span>
  <h1>AI 内容摘要</h1>
  <p class="lead">当日抓取 {total} 条 · 英文摘要附中文翻译 · 中文摘要直接展示</p>
  <div class="hero-meta">
    <div class="metric"><div class="metric-value">{total}</div><div class="metric-label">条目总数</div></div>
""")
    for sec_name in ("公司动态", "个人 Blog"):
        if sec_name in by_section_count:
            parts.append(
                f'    <div class="metric"><div class="metric-value">'
                f'{by_section_count[sec_name]}</div>'
                f'<div class="metric-label">{escape(sec_name)}</div></div>\n'
            )
    parts.append(
        f'    <div class="metric"><div class="metric-value">{len(sources_set)}</div>'
        f'<div class="metric-label">信源</div></div>\n'
    )
    parts.append("  </div>\n</div>\n")

    section_order = ["公司动态", "个人 Blog", "新论文 — 关注作者", "新论文 — 关键词命中"]
    section_idx = 0
    for section in section_order:
        if section not in by_section:
            continue
        group = by_section[section]
        alt_class = " alt" if section_idx % 2 == 0 else ""
        section_idx += 1
        by_source: dict[str, list[dict]] = {}
        for it in group:
            by_source.setdefault(it["source"], []).append(it)
        parts.append(f"""
<section class="section{alt_class}">
  <div class="container">
    <h2>{escape(section)}</h2>
    <div class="section-meta">{len(group)} 条 · {len(by_source)} 个来源</div>
""")
        for source, sg in by_source.items():
            sid = slugify(source)
            parts.append(f"""    <div class="source-group" id="{sid}">
      <div class="source-header">
        <div class="source-name">{escape(source)}</div>
        <div class="source-count">{len(sg)} 条</div>
      </div>
""")
            for it in sg:
                parts.append(f"""      <div class="item">
        <a class="item-title" href="{escape(it["url"])}" target="_blank" rel="noopener">{escape(it["title"])}</a>
""")
                if it["en"]:
                    parts.append(
                        f'        <div class="item-summary">'
                        f'<span class="lang-tag">EN</span>{escape(it["en"])}</div>\n'
                    )
                if it["zh"]:
                    cls = "item-summary zh" if it["en"] else "item-summary"
                    label = "中文" if it["en"] else ""
                    tag = f'<span class="lang-tag">{label}</span>' if label else ""
                    parts.append(
                        f'        <div class="{cls}">'
                        f'{tag}{escape(it["zh"])}</div>\n'
                    )
                parts.append(
                    f'        <div class="item-url">{escape(it["url"])}</div>\n'
                    f'      </div>\n'
                )
            parts.append("    </div>\n")
        parts.append("  </div>\n</section>\n")

    parts.append("""
<footer>
  AIDigest · 内容来自原作者，链接版权归各来源所有
</footer>
</body>
</html>
""")
    return "".join(parts)


# ---- driver ----

def date_from_report(p: Path) -> str:
    return p.stem  # YYYY-MM-DD.md → YYYY-MM-DD


def build_one(report_path: Path) -> tuple[Path, Path]:
    date = date_from_report(report_path)
    items = parse_report(report_path)
    items = enrich(items)
    DIGESTS.mkdir(parents=True, exist_ok=True)
    md_path = DIGESTS / f"digest-{date}.md"
    html_path = DIGESTS / f"digest-{date}.html"
    md_path.write_text(render_md(date, items))
    html_path.write_text(render_html(date, items))
    print(f"  {date}: {len(items)} items → {md_path.name}, {html_path.name}")
    return md_path, html_path


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        target = argv[1]
        report = REPORTS / f"{target}.md"
        if not report.exists():
            print(f"no report for {target}", file=sys.stderr)
            return 1
        build_one(report)
    else:
        reports = sorted(REPORTS.glob("*.md"))
        if not reports:
            print("no reports/*.md found", file=sys.stderr)
            return 1
        for r in reports:
            build_one(r)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
