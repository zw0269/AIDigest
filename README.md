# AIDigest

每日抓取 AI 公司 blog、领域人物 blog、arXiv 论文，输出本地 Markdown 日报与 Notion 风格的双语 HTML 浏览页。

零云依赖：纯本地 Python + RSS / arXiv API + macOS launchd。不调任何 LLM API，摘要按需手工撰写。

## 当前覆盖

| 类别 | 来源 |
|---|---|
| 公司 blog | Anthropic, OpenAI, Google DeepMind, Transformer Circuits |
| 人物 blog | Andrej Karpathy, Simon Willison, Lilian Weng, Sebastian Raschka, Yoshua Bengio, Dario Amodei |
| 论文 | arXiv（cs.AI / cs.CL / cs.LG，关键词 + 关注作者）|
| 关注作者 | Geoffrey Hinton, Yann LeCun, Ilya Sutskever |

## 工作流：两阶段

```
[1] aidigest run             [2] build_digest + build_index
   抓取 → 去重 → 写 md     →     md → 双语 HTML → 索引页
```

**阶段 1**：每天 08:00 由 launchd 触发 `aidigest run`，把当日新增写入 `reports/YYYY-MM-DD.md`。

**阶段 2**：手动或链式触发 HTML 渲染 — `scripts/build_digest.py` 生成当日 digest HTML（英文摘要 + 中文翻译并列），`scripts/build_index.py` 扫描所有 digest 重建 `llm-ai/index.html` 索引首页。

## 快速开始

```bash
cd /Users/zw/work/project_test/AIDigest

# 一次性安装
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# 验证所有源
PYTHONPATH=src .venv/bin/python -m aidigest verify

# 首次：标记当前所有内容为已见
PYTHONPATH=src .venv/bin/python -m aidigest init

# 跑一次日报 + 渲染 HTML
./scripts/run.sh
.venv/bin/python scripts/build_digest.py
.venv/bin/python scripts/build_index.py

# 浏览
open llm-ai/index.html
```

## 自动化（每天 08:00）

```bash
cp scripts/com.zw.aidigest.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.zw.aidigest.plist
```

Mac 休眠错过的 job 唤醒后会自动补跑（`StartCalendarInterval` 行为，比 cron 友好）。

## 目录结构

```
AIDigest/
├── README.md                       # 本文
├── CLAUDE.md                       # 协作准则（Claude Code 自动加载）
├── requirements.txt
├── config/
│   └── sources.yaml                # 唯一需要改的配置：信源 + arXiv
├── src/aidigest/                   # 抓取核心
│   ├── cli.py                      # init / run / verify
│   ├── fetchers/{rss,html,arxiv_fetcher}.py
│   ├── state.py                    # SQLite 去重
│   └── render.py                   # md 模板渲染
├── scripts/                        # 渲染管线 + 自动化
│   ├── data.py                     # URL → 中文摘要 / 翻译 数据
│   ├── build_digest.py             # 单日 digest HTML
│   ├── build_index.py              # 日期索引页
│   ├── run.sh                      # launchd 包装
│   └── com.zw.aidigest.plist       # launchd 配置
├── templates/report.md.j2          # 日报模板
├── reports/YYYY-MM-DD.md           # 日报输出（gitignored）
├── llm-ai/                         # 文档与浏览页
│   ├── index.html                  # ★ 入口：日期索引
│   ├── digests/digest-YYYY-MM-DD.{md,html}
│   ├── project-guide.md            # 项目原理（架构、设计决策）
│   ├── user-guide.md               # 操作手册
│   └── summary.md                  # 项目文档总览
├── data/seen.sqlite                # 去重状态（gitignored）
└── logs/                           # 日志（gitignored）
```

## 增删信源

编辑 `config/sources.yaml`：

```yaml
companies:
  - name: 某公司
    type: rss          # 或 html
    url: https://example.com/feed.xml
    # html 类型需要补：
    # link_pattern: "^/blog/[^/]+$"   # 正则匹配 anchor href
```

改完先 `verify`，没问题再 `run`。新源若是 HTML 且文章无 RSS description，需要在 `data/translations/{date}.json` 的 `manual_summaries` 加中文摘要；RSS 有英文 description 时，`translations` 加中文翻译。

## 调 arXiv

`config/sources.yaml` 的 `arxiv` 段：

- `categories` — `cs.AI` / `cs.CL` / `cs.LG` 等
- `keywords` — OR 拼接，命中题目/摘要任一即收
- `authors` — 关注作者（不写 blog 的研究者用此追踪论文）
- `lookback_days` — 只取最近 N 天发布（默认 2）

## 已知限制

- **HTML 源脆弱**：Anthropic / Dario Amodei / Transformer Circuits 没 RSS，靠列表页 `link_pattern` 解析，站点改版会失效。`verify` 命令可以快速发现（返回 EMPTY）。
- **OpenAI 文章正文 403**：OpenAI 站启用 Cloudflare 反爬，单页 WebFetch 失败。摘要直接取自 RSS 的 `<description>`，足够使用。
- **首日空报告**：`init` 后第一次 `run` 会是空的（所有当前条目都标 seen），从次日开始才有增量。
- **HTML 渲染需手动触发**：`aidigest run` 只产 md。HTML 渲染 (`build_digest.py` + `build_index.py`) 目前需手动运行；要全自动可在 `scripts/run.sh` 末尾追加这两行。

## 文档

- [`llm-ai/project-guide.md`](llm-ai/project-guide.md) — 架构、设计决策、为什么这么做
- [`llm-ai/user-guide.md`](llm-ai/user-guide.md) — 日常操作、改信源、故障排查、速查表
- [`llm-ai/summary.md`](llm-ai/summary.md) — 项目文档总览
- [`llm-ai/index.html`](llm-ai/index.html) — 浏览所有日期的日报（在浏览器打开）
