"""扫 llm-ai/digests/digest-*.html，生成 llm-ai/index.html 作为日期索引页。

每张卡片显示：日期 + 总条数 + 公司/个人 分布 + 信源数 + 几条预览 → 点击进入当日 digest。
"""

import re
import sys
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIGESTS = ROOT / "llm-ai" / "digests"
OUT = ROOT / "llm-ai" / "index.html"

DATE_RE = re.compile(r"digest-(\d{4}-\d{2}-\d{2})\.html$")


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
  --shadow-deep: rgba(0,0,0,0.01) 0 1px 3px,
                 rgba(0,0,0,0.02) 0 3px 7px,
                 rgba(0,0,0,0.02) 0 7px 15px,
                 rgba(0,0,0,0.04) 0 14px 28px,
                 rgba(0,0,0,0.05) 0 23px 52px;
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

.hero { padding: 96px 24px 64px; text-align: center; background: var(--bg); }
.hero-eyebrow {
  display: inline-block; padding: 4px 10px;
  background: var(--badge-bg); color: var(--badge-text);
  border-radius: 9999px; font-size: 12px; font-weight: 600;
  letter-spacing: 0.125px; margin-bottom: 24px;
}
.hero h1 {
  font-size: 64px; font-weight: 700; line-height: 1.0;
  letter-spacing: -2.125px; color: var(--text); margin-bottom: 20px;
}
.hero p.lead {
  font-size: 20px; font-weight: 400; line-height: 1.4;
  letter-spacing: -0.125px; color: var(--text-muted);
  max-width: 720px; margin: 0 auto 40px;
}
.hero-meta { display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; }
.metric {
  background: var(--bg); border: var(--whisper); border-radius: 12px;
  padding: 16px 24px; min-width: 140px; box-shadow: var(--shadow-card);
}
.metric-value {
  font-size: 32px; font-weight: 700; line-height: 1.0;
  letter-spacing: -0.5px; color: var(--text);
}
.metric-label {
  font-size: 12px; font-weight: 500; color: var(--text-muted);
  margin-top: 6px; letter-spacing: 0.125px;
}

section.section { padding: 80px 0; background: var(--bg-warm); }
section.section h2 {
  font-size: 40px; font-weight: 700; line-height: 1.05;
  letter-spacing: -1.25px; color: var(--text); margin-bottom: 12px;
}
section.section .section-meta {
  font-size: 14px; font-weight: 500; color: var(--text-muted); margin-bottom: 40px;
}

.day-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}
.day-card {
  display: block; background: var(--bg); border: var(--whisper);
  border-radius: 16px; padding: 24px 28px;
  box-shadow: var(--shadow-card);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.day-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-deep);
  text-decoration: none;
}
.day-card .day-date {
  font-size: 28px; font-weight: 700; line-height: 1.05;
  letter-spacing: -0.625px; color: var(--text); margin-bottom: 4px;
}
.day-card .day-count {
  display: inline-block; padding: 4px 10px;
  background: var(--badge-bg); color: var(--badge-text);
  border-radius: 9999px; font-size: 12px; font-weight: 600;
  letter-spacing: 0.125px; margin-bottom: 18px;
}
.day-card .day-stats {
  font-size: 14px; font-weight: 500; color: var(--text-muted);
  margin-bottom: 18px; line-height: 1.6;
}
.day-card .day-stats span {
  display: inline-block; margin-right: 10px;
}
.day-card .day-preview {
  margin-top: 14px; padding-top: 14px;
  border-top: var(--whisper);
  font-size: 13px; color: var(--text-muted); line-height: 1.5;
}
.day-card .day-preview-item {
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  margin-bottom: 4px;
}
.day-card .cta {
  margin-top: 18px; font-size: 14px; font-weight: 600;
  color: var(--blue);
}
.day-card:hover .cta { color: var(--blue-active); }

.empty {
  background: var(--bg); border: var(--whisper); border-radius: 16px;
  padding: 64px 32px; text-align: center;
  font-size: 16px; color: var(--text-muted);
}

footer {
  padding: 48px 24px 64px; border-top: var(--whisper);
  background: var(--bg);
  text-align: center; color: var(--text-muted); font-size: 14px;
}

@media (max-width: 768px) {
  .hero { padding: 64px 24px 48px; }
  .hero h1 { font-size: 40px; letter-spacing: -1.25px; }
  .hero p.lead { font-size: 18px; }
  section.section { padding: 56px 0; }
  section.section h2 { font-size: 30px; letter-spacing: -0.9px; }
  .day-grid { grid-template-columns: 1fr; gap: 16px; }
  .day-card { padding: 20px 22px; }
  .day-card .day-date { font-size: 24px; }
}
"""


def _html_text(html: str, selector_re: str, max_n: int) -> list[str]:
    return [
        re.sub(r"<[^>]+>", "", m).strip()
        for m in re.findall(selector_re, html, re.DOTALL)
    ][:max_n]


def parse_digest(p: Path) -> dict:
    """Pull stats from a digest html (regex-only — no extra deps)."""
    html = p.read_text()
    m = DATE_RE.search(p.name)
    date = m.group(1) if m else p.stem

    # total = count of div class="item"
    total = len(re.findall(r'<div class="item">', html))

    # per-section: H2 + section-meta count
    sections: dict[str, int] = {}
    for sec_match in re.finditer(
        r'<section class="section[^"]*">.*?<h2>([^<]+)</h2>\s*<div class="section-meta">(\d+) 条',
        html,
        re.DOTALL,
    ):
        sections[sec_match.group(1).strip()] = int(sec_match.group(2))

    # source count: count of source-group divs
    source_count = len(re.findall(r'class="source-group"', html))

    # preview titles (first 3)
    titles = _html_text(html, r'<a class="item-title"[^>]*>(.*?)</a>', 3)

    return {
        "date": date,
        "filename": p.name,
        "total": total,
        "sections": sections,
        "source_count": source_count,
        "preview_titles": titles,
    }


def render_index(days: list[dict]) -> str:
    total_items = sum(d["total"] for d in days)
    total_sources = max((d["source_count"] for d in days), default=0)

    parts: list[str] = []
    parts.append(f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AIDigest — 日报索引</title>
<style>{CSS}</style>
</head>
<body>

<div class="hero">
  <span class="hero-eyebrow">AIDigest · 索引</span>
  <h1>AI 日报索引</h1>
  <p class="lead">每日抓取 AI 公司 blog、人物 blog、arXiv 论文的摘要总览。点击日期卡片查看当日全部内容。</p>
  <div class="hero-meta">
    <div class="metric"><div class="metric-value">{len(days)}</div><div class="metric-label">天数</div></div>
    <div class="metric"><div class="metric-value">{total_items}</div><div class="metric-label">条目总数</div></div>
    <div class="metric"><div class="metric-value">{total_sources}</div><div class="metric-label">每日信源</div></div>
  </div>
</div>

<section class="section">
  <div class="container">
    <h2>所有日期</h2>
    <div class="section-meta">按日期倒序，最新的在前</div>
""")

    if not days:
        parts.append('    <div class="empty">还没有日报。跑 <code>aidigest run</code> 生成第一份。</div>\n')
    else:
        parts.append('    <div class="day-grid">\n')
        for d in days:
            stats = []
            for key in ("公司动态", "个人 Blog", "新论文 — 关注作者", "新论文 — 关键词命中"):
                if key in d["sections"]:
                    stats.append(f'<span>{escape(key)} {d["sections"][key]}</span>')
            preview_html = ""
            if d["preview_titles"]:
                preview_html = '<div class="day-preview">\n'
                for t in d["preview_titles"]:
                    preview_html += f'        <div class="day-preview-item">· {escape(t)}</div>\n'
                preview_html += "      </div>"
            parts.append(f"""      <a class="day-card" href="digests/{escape(d["filename"])}">
        <div class="day-date">{escape(d["date"])}</div>
        <div class="day-count">{d["total"]} 条</div>
        <div class="day-stats">{"".join(stats)}</div>
        {preview_html}
        <div class="cta">查看完整摘要 →</div>
      </a>
""")
        parts.append("    </div>\n")

    parts.append("""  </div>
</section>

<footer>
  AIDigest · 内容来自原作者，链接版权归各来源所有
</footer>
</body>
</html>
""")
    return "".join(parts)


def main() -> int:
    if not DIGESTS.exists():
        print(f"no digests dir at {DIGESTS}", file=sys.stderr)
        return 1
    files = sorted(DIGESTS.glob("digest-*.html"), reverse=True)
    days = [parse_digest(p) for p in files]
    OUT.write_text(render_index(days))
    print(f"wrote {OUT} ({len(days)} days, {sum(d['total'] for d in days)} items)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
