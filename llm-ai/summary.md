# AIDigest 文档总览

本项目当前共有 4 份核心 Markdown 文档。以下为每份的摘要与核心内容。

---

## 1. `README.md` — 项目入口

**性质**：项目根目录的快速上手说明，1-2 分钟读完。

**核心内容**：
- **目标**：每日抓取 AI 公司 blog（Anthropic / OpenAI / DeepMind）、人物 blog（Karpathy、Simon Willison、Lilian Weng 等）、arXiv 关键词 + 关注作者，输出本地 Markdown 日报。
- **设计层级**：第一层纯标题 + 来源 + 链接，自己挑感兴趣的深读，不做 LLM 摘要。
- **目录结构**：`config/`（信源配置）、`src/aidigest/`（代码）、`reports/`（日报输出）、`scripts/`（launchd）、`data/`（SQLite 去重）。
- **安装**：`python3 -m venv .venv` + `pip install -r requirements.txt`。
- **三个子命令**：`verify`（检查源）、`init`（首次标记历史为已见）、`run`（生成今日日报）。
- **自动化**：copy plist 到 `~/Library/LaunchAgents/` + `launchctl load`，每天 08:00 触发，Mac 休眠会唤醒后补跑。
- **已知限制**：Anthropic / Dario Amodei 没 RSS 用 HTML 解析（改版会失效）；首次 `init` 后第一份报告会是空的。

---

## 2. `llm-ai/project-guide.md` — 项目指南

**性质**：讲"为什么这么做"，给想理解架构 / 二次开发的人看。

**核心内容**：
- **设计原则**：零三方服务、RSS 优先 HTML 兜底、只列增量、单源失败不影响整体、配置即代码（YAML）。
- **架构图**：`sources.yaml → fetchers (rss/html/arxiv) → SQLite 去重 → render → reports/YYYY-MM-DD.md`。
- **信源策略**：公司 blog 大多 RSS，Anthropic 用 `/news` 列表页 HTML 解析；个人 blog Hinton/LeCun/Sutskever 不写博客，改用 arXiv 作者订阅替代。
- **关键决策与理由**：
  - SQLite vs JSON：主键查询效率，库小用不着 Postgres
  - arXiv lookback=2 天 vs RSS=14 天：arXiv 量大，RSS 14 天主要是首次 init 时不被 OpenAI 929 条历史压垮
  - canonical URL 作 ID：跨源同一篇论文统一规范化为 `arxiv:2401.12345`
  - 不做摘要：第一层是信息流，摘要会让人误以为读懂从而跳过原文
- **失败模式表**：每种失败的表现 + 处理方式（RSS 改 URL、HTML 改版、arXiv 限流、网络中断、Mac 休眠）。
- **演化方向**：周报 + LLM 摘要、Twitter/Nitter、关键词反馈循环、按主题分文件输出 — 都不在 MVP 范围。

---

## 3. `llm-ai/user-guide.md` — 用户操作指南

**性质**：日常操作手册，遇到问题先查这份。

**核心内容**：
- **一次性安装**：venv + pip install，约 30 MB。
- **三个子命令**：`verify` / `init` / `run`，各自用途与触发时机。
- **launchd 启用**：copy plist + load，立即触发用 `launchctl start`，改时间需 unload → 改文件 → load。
- **改信源**：在 `config/sources.yaml` 加 RSS 或 HTML 源，HTML 源需要写正则 `link_pattern` 匹配 anchor href。
- **调 arXiv**：`categories` / `keywords` / `authors` / `max_results_per_query` / `lookback_days` 五个参数；关键词调优原则（太宽噪声大、太窄漏召）；`au:` 同名干扰风险。
- **阅读日报**：`reports/YYYY-MM-DD.md` 分公司 / 个人 / arXiv 作者 / arXiv 关键词四段，推荐用 Obsidian 当 vault 积累笔记。
- **故障排查**：日报为空（两种原因）、源失效（HTTP 4xx / EMPTY）、重置（rm sqlite + init）、launchd 不跑（list / err.log / 手动跑脚本）。
- **日常使用建议**：早上喝咖啡时扫一眼 3-5 分钟；一周清理一次 `reports/`；每月调一次关键词。
- **速查表**：六个最常用命令一行对照。

---

## 4. `reports/2026-05-03.md` — 首份日报

**性质**：项目跑出的第一份真实产物。

**核心内容**：
- **总量**：78 条新内容。
- **公司动态**（44 条）：OpenAI 占大多数（GPT-5.5 发布、Codex 系列文档、企业合作），DeepMind（DiLoCo、co-clinician），Anthropic（Claude Opus 4.7、Claude Design、各种合作公告）。
- **个人 Blog**（34 条）：Simon Willison 高产（30 条，DeepSeek V4 评测、GPT-5.5 提示工程、Codex CLI 笔记），Dario Amodei 4 篇长文（The Adolescence of Technology、Machines of Loving Grace、Urgency of Interpretability、On DeepSeek and Export Controls）。
- **arXiv 关键词**：0 条（最近 2 天关键词未命中）。
- **arXiv 关注作者**：0 条（Hinton / LeCun / Sutskever 最近 2 天无新 paper，正常）。
- **缺席**：Karpathy、Lilian Weng、Sebastian Raschka、Bengio 最近 14 天未更新。

---

## 项目状态速览

| 维度 | 状态 |
|---|---|
| 信源数 | 9（3 公司 + 6 个人） + arXiv（关键词 + 3 位作者） |
| 代码量 | ~400 行 Python |
| 依赖 | feedparser, httpx, selectolax, arxiv, PyYAML, Jinja2 |
| 调度 | launchd 每天 08:00（待用户安装 plist） |
| 去重 | SQLite，已 seed 78 条 |
| 报告输出 | 本地 Markdown，路径 `reports/YYYY-MM-DD.md` |
