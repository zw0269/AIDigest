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

### 1.5 补 GitHub 短描述（写中文前）

GitHub Trending 的描述就是仓库 About，偶尔极短或为空（如 `git push no-mistakes`），
只看标题写中文容易臆测出错。跑下面脚本，自动给 **描述短于 30 字** 的 GitHub 条目
抓 README 正文摘录（拿不到再用 GitHub API 兑底），写到 `reports/YYYY-MM-DD.enrich.md` 旁注：

```bash
./.venv/bin/python scripts/enrich_short_descs.py YYYY-MM-DD   # 可加 --threshold N
```

第 2 步给这些 GitHub 条目写 `manual_summaries` 时，**先读这个旁注**再下笔。
旁注落在 `reports/`（已 gitignore），不提交、不进 digest。若输出提示 `GitHub API 限流 403`，
设 `GITHUB_TOKEN` 后重试即可（README 走 raw CDN 一般不受限）。

### 2. 补中文翻译（CLAUDE.md 规则 6）

读 `reports/YYYY-MM-DD.md` 看新条目。每条都必须在渲染产物里有 `中文:` 行（包括 arXiv 论文）。

所有翻译写进 `data/translations/YYYY-MM-DD.json`（不存在就新建，存在就读出来加 key 再整体写回，注意保证输出是合法 JSON），结构固定：
```json
{
  "manual_summaries": {"https://...": "中文摘要...", ...},
  "translations": {"https://...": "中文翻译...", ...}
}
```
`data/seen.sqlite` 保证同一 URL 只会被抓一次，所以新条目不会跟历史文件的 URL 重复，**不需要**翻旧的 `data/translations/*.json` 查重，直接往当天这个文件里加就行。

- **公司动态 / 个人 Blog（RSS 源）**：用 feedparser 拿到 RSS description（参考 `scripts/build_digest.py` 的 `rss_index()`），写一句中文概括加进 `translations`。
  - 仅有中文摘要的源（Anthropic、Dario Amodei 等）跳过。
  - HTML 源（无 RSS description）改加到 `manual_summaries`。
- **社区动态（GitHub Trending / Hacker News Newest / YouTube AI）**：标题里 GitHub 已经包含英文一句话描述（`owner/repo — desc`，描述过短的见第 1.5 步旁注），HN 只有标题，YouTube 已带「频道 — 标题（XXX,XXX 次播放）」。三者都没有 RSS description，每条都要写一句中文摘要加到 `manual_summaries`，key 是条目 url（GitHub 是 repo 主页、HN 是 `news.ycombinator.com/item?id=N`、YouTube 是 `https://www.youtube.com/watch?v=VID`）。YouTube 标题已含频道和播放量，中文写一句视频核心内容即可。
- **arXiv 论文**：report 只存了 title/url，必须用 `arxiv` 库按 ID 批量拉 `summary`，再写一句中文核心要点加进 `translations`，key 用完整 `result.entry_id`（含 `v1` 等后缀）。

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

YouTube 视频如需进一步看 description（决定中文摘要怎么写）：

```bash
.venv/bin/python -c "
from yt_dlp import YoutubeDL
ids = ['VIDEO_ID_1', 'VIDEO_ID_2']  # 从 reports/YYYY-MM-DD.md 复制 watch?v= 后面
opts = {'quiet': True, 'no_warnings': True, 'skip_download': True}
with YoutubeDL(opts) as ydl:
    for vid in ids:
        info = ydl.extract_info(f'https://www.youtube.com/watch?v={vid}', download=False)
        print('VID::', vid)
        print('TITLE::', info.get('title'))
        print('DESC::', (info.get('description') or '')[:500].replace(chr(10),' '))
        print('---')
"
```

批量取 arXiv abstract 的 one-liner（把所有新论文 ID 喂进去）：

```bash
.venv/bin/python -c "
import arxiv
ids = ['2605.04039v1', '2605.04036v1']  # 从 reports/YYYY-MM-DD.md 复制 arxiv URL 末尾
client = arxiv.Client(page_size=50, delay_seconds=3, num_retries=3)
for r in client.results(arxiv.Search(id_list=ids)):
    print('URL::', r.entry_id)
    print('TITLE::', r.title.strip().replace(chr(10),' '))
    print('ABS::', r.summary.strip().replace(chr(10),' '))
    print('---')
"
```

### 3. 渲染 HTML

```bash
PYTHONPATH=src ./.venv/bin/python scripts/build_digest.py YYYY-MM-DD
PYTHONPATH=src ./.venv/bin/python scripts/build_index.py
```

抽查产物：`grep -c "中文:" llm-ai/digests/digest-YYYY-MM-DD.md` 必须等于当日条目总数（含论文）。缺了回到第 2 步补。

### 4. Git commit

只 stage 本次相关文件，不要 `git add -A`：

```bash
git add llm-ai/index.html \
        llm-ai/digests/digest-YYYY-MM-DD.md \
        llm-ai/digests/digest-YYYY-MM-DD.html \
        data/translations/YYYY-MM-DD.json
git commit -m "content: 抓取 MM-DD 新增 N 条 ..."
```

提交信息沿用 `git log --oneline -10` 中既有风格（`content:` / `docs+content:` 前缀），一句话点出新增条目主题。**不要 push**（除非用户明确要求）。

注意：`reports/YYYY-MM-DD.md` 和 `data/seen.sqlite` 在 `.gitignore` 中，不会也不要提交。

### 5. 报告

向用户简短汇报：日期、新增条数、来源、是否写了 data/translations/YYYY-MM-DD.json、commit hash。
