"""读 config/sources.yaml + CLAUDE.md，渲染 llm-ai/sources-and-rules.html。

每次改信源或规则后都要重跑此脚本（CLAUDE.md 规则 8）。
"""

import re
import sys
from html import escape
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "sources.yaml"
CLAUDE_MD = ROOT / "CLAUDE.md"
OUT = ROOT / "llm-ai" / "sources-and-rules.html"


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
  --code-bg: #f4f3f1;
  --whisper: 1px solid rgba(0,0,0,0.1);
  --shadow-card: rgba(0,0,0,0.04) 0 4px 18px,
                 rgba(0,0,0,0.027) 0 2.025px 7.84688px,
                 rgba(0,0,0,0.02) 0 0.8px 2.925px,
                 rgba(0,0,0,0.01) 0 0.175px 1.04062px;
  --font: "NotionInter", Inter, -apple-system, system-ui, "Segoe UI", Helvetica,
          "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font); font-size: 16px; line-height: 1.6;
  color: var(--text); background: var(--bg);
  -webkit-font-smoothing: antialiased;
}
a { color: var(--blue); text-decoration: none; word-break: break-all; }
a:hover { text-decoration: underline; }
code {
  background: var(--code-bg); padding: 2px 6px; border-radius: 4px;
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  font-size: 0.92em;
}

.container { max-width: 1080px; margin: 0 auto; padding: 0 24px; }

.hero { padding: 72px 24px 48px; text-align: center; }
.hero-eyebrow {
  display: inline-block; padding: 4px 10px;
  background: var(--badge-bg); color: var(--badge-text);
  border-radius: 9999px; font-size: 12px; font-weight: 600;
  margin-bottom: 20px;
}
.hero h1 {
  font-size: 56px; font-weight: 700; line-height: 1.05;
  letter-spacing: -1.75px; margin-bottom: 16px;
}
.hero p.lead {
  font-size: 18px; color: var(--text-muted);
  max-width: 720px; margin: 0 auto;
}
.hero-nav { margin-top: 24px; font-size: 14px; }
.hero-nav a { margin: 0 10px; }

section.section { padding: 56px 0; }
section.section + section.section { padding-top: 0; }
section.section h2 {
  font-size: 32px; font-weight: 700; line-height: 1.1;
  letter-spacing: -1px; margin-bottom: 8px;
}
section.section .section-meta {
  font-size: 14px; color: var(--text-muted); margin-bottom: 28px;
}

.card-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
}
.card {
  background: var(--bg); border: var(--whisper); border-radius: 12px;
  padding: 20px 24px; box-shadow: var(--shadow-card);
}
.card .card-title {
  font-size: 18px; font-weight: 600; margin-bottom: 6px;
}
.card .card-meta {
  font-size: 12px; color: var(--text-dim); margin-bottom: 8px;
  text-transform: uppercase; letter-spacing: 0.5px;
}
.card .card-url {
  font-size: 13px; color: var(--text-muted);
}

.tag {
  display: inline-block; padding: 2px 8px; border-radius: 9999px;
  background: var(--code-bg); color: var(--text-muted);
  font-size: 11px; font-weight: 600;
  margin-right: 6px; letter-spacing: 0.3px;
}
.tag.rss { background: #fff4e6; color: #b25c00; }
.tag.html { background: #eaf5ff; color: #0075de; }
.tag.gh { background: #f0f0f0; color: #24292f; }
.tag.hn { background: #fff0e6; color: #ff6600; }

.kv-list {
  background: var(--bg-warm); border-radius: 12px;
  padding: 20px 24px; font-size: 14px; line-height: 1.8;
}
.kv-list .kv { margin-bottom: 6px; }
.kv-list .kv-key {
  display: inline-block; min-width: 200px;
  font-weight: 600; color: var(--text-muted);
}

.rule {
  background: var(--bg-warm); border-radius: 12px;
  padding: 24px 28px; margin-bottom: 16px;
}
.rule h3 {
  font-size: 20px; font-weight: 700; margin-bottom: 12px;
  letter-spacing: -0.3px;
}
.rule p { margin-bottom: 10px; }
.rule p strong { font-weight: 700; }
.rule ul { padding-left: 22px; margin-bottom: 10px; }
.rule ul li { margin-bottom: 4px; }
.rule pre {
  background: #1f1e1c; color: #eae6e1; padding: 14px 18px;
  border-radius: 8px; overflow-x: auto; margin: 10px 0;
  font-size: 13px; line-height: 1.55;
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
}
.rule pre code { background: transparent; padding: 0; color: inherit; }

footer {
  padding: 48px 24px 64px; border-top: var(--whisper);
  text-align: center; color: var(--text-muted); font-size: 14px;
}

@media (max-width: 768px) {
  .hero { padding: 48px 24px; }
  .hero h1 { font-size: 36px; letter-spacing: -1px; }
  .card-grid { grid-template-columns: 1fr; }
  .kv-list .kv-key { display: block; min-width: 0; }
}
"""


def _type_tag(t: str) -> str:
    label = {
        "rss": "RSS",
        "html": "HTML",
        "github_trending": "GitHub Trending",
        "hn_newest": "HN Newest",
    }.get(t, t)
    cls = {
        "rss": "rss",
        "html": "html",
        "github_trending": "gh",
        "hn_newest": "hn",
    }.get(t, "")
    return f'<span class="tag {cls}">{escape(label)}</span>'


def render_source_card(s: dict) -> str:
    return f"""    <div class="card">
      <div class="card-meta">{_type_tag(s.get("type", ""))}</div>
      <div class="card-title">{escape(s["name"])}</div>
      <div class="card-url"><a href="{escape(s["url"])}" target="_blank" rel="noopener">{escape(s["url"])}</a></div>
    </div>"""


def render_sources(cfg: dict) -> str:
    parts: list[str] = []

    def section(title: str, sources: list[dict]) -> None:
        parts.append(f"""<section class="section">
  <div class="container">
    <h2>{escape(title)}</h2>
    <div class="section-meta">{len(sources)} 个信源</div>
    <div class="card-grid">""")
        for s in sources:
            parts.append(render_source_card(s))
        parts.append("    </div>\n  </div>\n</section>\n")

    section("公司动态", cfg.get("companies", []))
    section("个人 Blog", cfg.get("individuals", []))
    section("社区动态", cfg.get("community", []))

    arx = cfg.get("arxiv", {}) or {}
    if arx:
        cats = ", ".join(arx.get("categories", []))
        kws = ", ".join(f"<code>{escape(k)}</code>" for k in arx.get("keywords", []))
        authors = ", ".join(f"<code>{escape(a)}</code>" for a in arx.get("authors", []))
        parts.append(f"""<section class="section">
  <div class="container">
    <h2>arXiv 论文</h2>
    <div class="section-meta">按 cs.* 分类 + 关键词 / 关注作者扫描</div>
    <div class="kv-list">
      <div class="kv"><span class="kv-key">分类 (categories)</span><code>{escape(cats)}</code></div>
      <div class="kv"><span class="kv-key">关键词 (keywords)</span>{kws}</div>
      <div class="kv"><span class="kv-key">关注作者 (authors)</span>{authors}</div>
      <div class="kv"><span class="kv-key">每查询最大数</span><code>{arx.get("max_results_per_query", "?")}</code></div>
      <div class="kv"><span class="kv-key">回溯天数</span><code>{arx.get("lookback_days", "?")}</code> 天</div>
    </div>
  </div>
</section>
""")

    lookback = cfg.get("rss_lookback_days")
    if lookback:
        parts.append(f"""<section class="section">
  <div class="container">
    <h2>全局抓取参数</h2>
    <div class="kv-list">
      <div class="kv"><span class="kv-key">RSS 回溯天数</span><code>{lookback}</code> 天</div>
    </div>
  </div>
</section>
""")
    return "".join(parts)


# ---- markdown → html (subset used in CLAUDE.md) ----

_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")


def _inline(text: str) -> str:
    text = escape(text)
    text = _BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = _INLINE_CODE_RE.sub(r"<code>\1</code>", text)
    return text


def md_to_html(md: str) -> str:
    """Tiny markdown subset: paragraphs, bullet lists, fenced code blocks, **bold**, `code`."""
    out: list[str] = []
    lines = md.splitlines()
    i = 0
    in_list = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_list:
                out.append("</ul>")
                in_list = False
            i += 1
            buf: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append(f"<pre><code>{escape(chr(10).join(buf))}</code></pre>")
            continue

        if stripped.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{_inline(stripped[2:])}</li>")
            i += 1
            continue

        if in_list:
            out.append("</ul>")
            in_list = False

        if not stripped:
            i += 1
            continue

        out.append(f"<p>{_inline(stripped)}</p>")
        i += 1

    if in_list:
        out.append("</ul>")
    return "\n".join(out)


_RULE_RE = re.compile(r"^## (\d+)\.\s+(.+)$")


def parse_rules(md: str) -> list[tuple[str, str, str]]:
    """Returns [(num, title, body_md), ...]."""
    lines = md.splitlines()
    rules: list[tuple[str, str, str]] = []
    cur_num = ""
    cur_title = ""
    cur_body: list[str] = []
    for line in lines:
        m = _RULE_RE.match(line)
        if m:
            if cur_num:
                rules.append((cur_num, cur_title, "\n".join(cur_body).strip()))
            cur_num = m.group(1)
            cur_title = m.group(2).strip()
            cur_body = []
        elif cur_num:
            if line.strip() == "---":
                rules.append((cur_num, cur_title, "\n".join(cur_body).strip()))
                cur_num = ""
                cur_body = []
            else:
                cur_body.append(line)
    if cur_num:
        rules.append((cur_num, cur_title, "\n".join(cur_body).strip()))
    return rules


def render_rules(md: str) -> str:
    rules = parse_rules(md)
    parts = [f"""<section class="section">
  <div class="container">
    <h2>项目规则（CLAUDE.md）</h2>
    <div class="section-meta">共 {len(rules)} 条 — 单一来源就是 <code>CLAUDE.md</code></div>
"""]
    for num, title, body in rules:
        parts.append(f"""    <div class="rule">
      <h3>{escape(num)}. {escape(title)}</h3>
      {md_to_html(body)}
    </div>
""")
    parts.append("  </div>\n</section>\n")
    return "".join(parts)


def render_page(cfg: dict, claude_md: str) -> str:
    n_companies = len(cfg.get("companies", []))
    n_individuals = len(cfg.get("individuals", []))
    n_community = len(cfg.get("community", []))
    n_rules = len(parse_rules(claude_md))
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AIDigest — 信源 & 规则</title>
<style>{CSS}</style>
</head>
<body>

<div class="hero">
  <span class="hero-eyebrow">AIDigest · 配置</span>
  <h1>信源 & 规则</h1>
  <p class="lead">所有抓取信源（公司动态、个人 Blog、社区动态、arXiv 论文）和 CLAUDE.md 项目规则的总览。</p>
  <p class="lead" style="font-size:14px;margin-top:8px;color:var(--text-dim)">
    {n_companies} 公司 · {n_individuals} 个人 · {n_community} 社区 · {n_rules} 规则
  </p>
  <div class="hero-nav">
    <a href="index.html">← 日报索引</a>
  </div>
</div>

{render_sources(cfg)}

{render_rules(claude_md)}

<footer>
  本页由 <code>scripts/build_sources_rules.py</code> 自动生成，改信源/规则后请重跑。
</footer>
</body>
</html>
"""


def main() -> int:
    cfg = yaml.safe_load(CONFIG.read_text())
    claude_md = CLAUDE_MD.read_text()
    OUT.write_text(render_page(cfg, claude_md))
    n_rules = len(parse_rules(claude_md))
    n_sources = (
        len(cfg.get("companies", []))
        + len(cfg.get("individuals", []))
        + len(cfg.get("community", []))
    )
    print(f"wrote {OUT} ({n_sources} sources + arxiv config, {n_rules} rules)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
