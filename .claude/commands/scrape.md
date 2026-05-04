---
description: 抓取所有信源新增内容 → 补中文翻译 → 渲染 HTML → git commit
---

# /scrape — AIDigest 一键抓取流程

执行 AIDigest 项目的完整日常抓取流程。当用户说"抓取信息"/"跑日报"/"更新 digest"等同义请求时，按下面步骤执行。

## 步骤

### 1. 抓取（自动去重）

```bash
bash scripts/run.sh
```

输出形如 `Wrote .../reports/YYYY-MM-DD.md (N new items, 0 errors)`，记下 N 和日期。
SQLite (`data/seen.sqlite`) 已经处理去重，跑过的不会重复入库。

如果 N == 0：跳到第 5 步报告"无新增"，结束。

### 2. 补中文翻译（CLAUDE.md 规则 6）

读 `reports/YYYY-MM-DD.md` 看新条目。对每条：

- **公司动态 / 个人 Blog（RSS 源）**：检查 `scripts/data.py` 的 `TRANSLATIONS` 是否已有对应 URL。没有的话用 feedparser 拿到 RSS description（参考 `scripts/build_digest.py` 的 `rss_index()`），再写一句中文概括加进 `TRANSLATIONS`。
  - 仅有中文摘要的源（Anthropic、Dario Amodei 等）跳过。
  - HTML 源（无 RSS description）改加到 `MANUAL_SUMMARIES`。
- **arXiv 论文**：标题已是英文，无需 description；不必补 TRANSLATIONS。

快速取 RSS description 的 one-liner：

```bash
.venv/bin/python -c "
import feedparser, re
from html import unescape
f = feedparser.parse('<RSS_FEED_URL>')
for e in f.entries:
    if '<URL_KEYWORD>' in e.link:
        d = getattr(e,'description','') or getattr(e,'summary','')
        print(e.link); print(unescape(re.sub(r'<[^>]+>','',d)).strip()[:600])
        break
"
```

### 3. 渲染 HTML

```bash
PYTHONPATH=src ./.venv/bin/python scripts/build_digest.py YYYY-MM-DD
PYTHONPATH=src ./.venv/bin/python scripts/build_index.py
```

抽查产物：`grep "EN\|中文" llm-ai/digests/digest-YYYY-MM-DD.md` — 每条带 EN 的下一行必须有 `中文:`。缺了回到第 2 步补。

### 4. Git commit

只 stage 本次相关文件，不要 `git add -A`：

```bash
git add llm-ai/index.html \
        llm-ai/digests/digest-YYYY-MM-DD.md \
        llm-ai/digests/digest-YYYY-MM-DD.html \
        scripts/data.py        # 仅当本次改了 TRANSLATIONS/MANUAL_SUMMARIES
git commit -m "content: 抓取 MM-DD 新增 N 条 ..."
```

提交信息沿用 `git log --oneline -10` 中既有风格（`content:` / `docs+content:` 前缀），一句话点出新增条目主题。**不要 push**（除非用户明确要求）。

注意：`reports/YYYY-MM-DD.md` 和 `data/seen.sqlite` 在 `.gitignore` 中，不会也不要提交。

### 5. 报告

向用户简短汇报：日期、新增条数、来源、是否补了 TRANSLATIONS、commit hash。
