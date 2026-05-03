# AIDigest 项目指南

## 这是什么

每天自动抓取 AI 领域几个固定来源的更新，输出一份本地 Markdown 日报。

第一层只列**标题 + 来源 + 链接**，不做摘要、不做翻译、不做评分 — 你自己扫，挑感兴趣的去原文深读。

## 设计原则

1. **零依赖第三方服务**：不调 LLM API，不依赖云函数，纯本地 Python + macOS launchd。日报里不会有"AI 替你筛选"的失真。
2. **RSS 优先，HTML 兜底**：不用 Playwright 之类的反爬重武器。所有源都能用 `feedparser` 或 `httpx + selectolax` 解决。
3. **只列增量**：SQLite 记录已见条目，每天 run 只输出新增。第一天 init 后第一份报告会是空的，正常。
4. **失败不影响整体**：单个源挂了，其他源继续，错误写到日报顶部告警。
5. **配置即代码**：增删信源 = 改 YAML，不需要写代码。

## 架构

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  config/     │    │  fetchers/   │    │  state.py    │
│  sources.yaml│ →  │  rss / html  │ →  │  SQLite 去重 │
└──────────────┘    │  arxiv       │    └──────┬───────┘
                    └──────────────┘           │
                                               ↓
                    ┌──────────────────────────────────┐
                    │  render.py + report.md.j2        │
                    │  → reports/YYYY-MM-DD.md         │
                    └──────────────────────────────────┘
```

调用入口：`python -m aidigest {init|run|verify}`，由 `scripts/run.sh` 包装，由 `scripts/com.zw.aidigest.plist` 每天 08:00 触发。

## 信源策略

| 类别 | 实现 | 备注 |
|---|---|---|
| 公司 blog | RSS（OpenAI、DeepMind）+ HTML（Anthropic） | Anthropic 没有公开 RSS，从 `/news` 列表页解析 `<a href="/news/...">` |
| 个人 blog | RSS（Karpathy、Simon Willison、Lilian Weng、Sebastian Raschka、Bengio）+ HTML（Dario Amodei） | Hinton / LeCun / Sutskever 不写 blog，改用 arXiv 作者订阅 |
| 论文 | arXiv 官方 API | 两个查询：分类 + 关键词 OR；分类 + 作者名 |

**为什么不用 Twitter / X**：API 收费贵、反爬严、签名复杂，性价比低。LeCun、Karpathy 在 X 上发的内容大多也会归档到他们的 blog 或 arXiv，错过的代价低。

## 关键设计决策

### 为什么 SQLite 而不是 JSON / 时间戳文件

去重要按 `id` 主键查询，SQLite 一行 SQL 搞定，JSON 要全文加载比较低效。库本身只有几 MB，用不着 Postgres。

### 为什么 arXiv lookback = 2 天，RSS lookback = 14 天

- arXiv 量大（每天 cs.AI/CL/LG 加起来上百篇），只看最近 2 天足够日报量级
- RSS 量小，14 天窗口主要是为**首次 init 时不被 OpenAI 929 条历史压垮**。日常 run 因为 SQLite 去重，窗口大小其实无关紧要。

### 为什么 ID 用 canonical URL 而不是 GUID

跨源同一篇论文可能在 arXiv API、Karpathy 的 blog、Simon 的快讯里都出现。统一规范化为 `arxiv:2401.12345` 或 `host/path` 才能去重。GUID 是源专属的，跨源会失效。

### 为什么不做摘要

第一层是"信息流"，第二层是"深度阅读"。摘要会让你**误以为**已经读懂了，反而跳过原文。如果以后想要摘要，单独跑一个 `digest --weekly --summarize` 命令对周报做即可。

## 失败模式与监测

| 失败 | 表现 | 处理 |
|---|---|---|
| RSS feed 改 URL | `verify` 报 EMPTY 或 FAIL | 改 `sources.yaml` |
| HTML 站改版 | `verify` 报 EMPTY | 重新看 HTML 结构，改 `link_pattern` 或 `_extract_title` |
| arXiv API 限流 | 日志报错，单次抓取失败 | `arxiv` 库内置 3 次重试 + 3 秒延迟，通常自愈 |
| 网络中断 | run 退出非 0 | launchd 不会重试，但明天会再跑（错过的条目会在明天补 — 已 mark seen 之前不会丢） |
| Mac 休眠错过 08:00 | 唤醒后 launchd 自动补跑 | `StartCalendarInterval` 行为，不需要额外处理 |

## 文件清单

```
AIDigest/
├── README.md                    # 快速上手
├── llm-ai/
│   ├── project-guide.md         # 本文：项目原理
│   └── user-guide.md            # 日常操作手册
├── requirements.txt             # 6 个依赖
├── config/
│   └── sources.yaml             # 唯一需要改的配置
├── src/aidigest/
│   ├── cli.py                   # 入口 + 三个子命令
│   ├── models.py                # Item 数据类
│   ├── state.py                 # SQLite 封装
│   ├── dedupe.py                # canonical_id() + dedupe()
│   ├── render.py                # Jinja2 渲染
│   └── fetchers/
│       ├── rss.py               # feedparser
│       ├── html.py              # httpx + selectolax
│       └── arxiv_fetcher.py     # arxiv 库
├── templates/
│   └── report.md.j2             # 日报模板
├── scripts/
│   ├── run.sh                   # launchd 调用包装
│   └── com.zw.aidigest.plist    # launchd 配置
├── data/seen.sqlite             # 去重状态（gitignore）
├── logs/                        # 日志（gitignore）
└── reports/YYYY-MM-DD.md        # 日报输出（gitignore）
```

## 演化方向（如果以后想扩）

- **Weekly 周报**：累积一周条目，调 Claude API 做主题聚类 + 中文摘要
- **更多人物**：Twitter 抓取改用 Nitter 镜像 RSS（`nitter.<instance>/<user>/rss`）
- **关键词反馈循环**：记录哪些 arXiv 命中你点进去看了（手动标记 `seen.sqlite`），用来调词表
- **多分类输出**：按主题分文件（`reports/2026-05-03/papers.md`、`/companies.md`）

但这些都不在 MVP 范围 — 先稳定跑两周，看实际产出再决定。
