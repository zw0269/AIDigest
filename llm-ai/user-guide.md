# AIDigest 用户操作指南

## 0. 一次性安装

```bash
cd /Users/zw/work/project_test/AIDigest
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

完成后 `.venv/` 占用约 30 MB。

## 1. 三个子命令

所有命令都从 AIDigest 根目录运行：

```bash
# 检查所有源是否能正常拉到内容
PYTHONPATH=src .venv/bin/python -m aidigest verify

# 把当前所有条目标记为"已见"，不生成日报
# 只在首次部署或重置时用
PYTHONPATH=src .venv/bin/python -m aidigest init

# 抓取新条目，写入 reports/YYYY-MM-DD.md
PYTHONPATH=src .venv/bin/python -m aidigest run
```

`scripts/run.sh` 是 `run` 命令的封装，launchd 调用的就是它。

## 2. 启用每天自动跑

```bash
cp scripts/com.zw.aidigest.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.zw.aidigest.plist
```

默认每天 **08:00** 触发。Mac 休眠错过会在唤醒后补跑。

### 立即触发一次（测试 plist 是否生效）

```bash
launchctl start com.zw.aidigest
```

跑完后看 `reports/YYYY-MM-DD.md` 和 `logs/launchd.out.log`。

### 改时间

编辑 `scripts/com.zw.aidigest.plist` 里的 `Hour` 和 `Minute`，然后：

```bash
launchctl unload ~/Library/LaunchAgents/com.zw.aidigest.plist
cp scripts/com.zw.aidigest.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.zw.aidigest.plist
```

### 查看是否在运行

```bash
launchctl list | grep aidigest
# 输出形如: -  0  com.zw.aidigest
# 第一个数字是 PID（- 表示当前没在跑），第二个是上次退出码（0 = 正常）
```

### 停用

```bash
launchctl unload ~/Library/LaunchAgents/com.zw.aidigest.plist
```

## 3. 改信源

编辑 `config/sources.yaml`。

### 加一个有 RSS 的源

```yaml
individuals:
  - name: 张三
    type: rss
    url: https://example.com/feed.xml
```

### 加一个没 RSS 的 HTML 源

```yaml
companies:
  - name: 某公司
    type: html
    url: https://example.com/blog
    link_pattern: "^/blog/[^/]+$"   # 正则匹配 <a href> 的路径部分
```

`link_pattern` 是 Python 正则，匹配 anchor 的 `href`。要找对的话：
1. 浏览器打开列表页，"查看源代码"
2. 找一个文章链接，看 `href` 长什么样
3. 写正则匹配该格式

### 改完之后

```bash
PYTHONPATH=src .venv/bin/python -m aidigest verify
```

确保新源 OK 后，下次 `run` 就会包含它。

## 4. 调 arXiv

`config/sources.yaml` 的 `arxiv:` 段：

```yaml
arxiv:
  categories: [cs.AI, cs.CL, cs.LG]   # arXiv 分类，决定抓取范围
  keywords:                            # 关键词，OR 拼接，命中任一就收
    - "large language model"
    - "agent"
    - "reasoning"
  authors:                             # 关注的作者
    - "Geoffrey Hinton"
    - "Yann LeCun"
  max_results_per_query: 30            # 每次查询最多返回多少条
  lookback_days: 2                     # 只看最近 N 天发布的
```

**关键词调优原则**：
- 太宽（`AI`, `model`）→ 噪声大
- 太窄（`Mixture-of-Recursion-Experts`）→ 漏召
- 一开始保守一点，跑两周看哪些命中你会点开看，再加/删

**作者搜索的限制**：arXiv 的 `au:` 查询是按字符串匹配，不是同名消歧。`"Yann LeCun"` 是稳的，但常见英文名（如 `"John Smith"`）会有同名干扰。

## 5. 阅读日报

`reports/2026-05-03.md` 结构：

```
# AI Digest — 2026-05-03

## 公司动态
- **OpenAI** — [GPT-5.5 System Card](https://openai.com/index/gpt-5-5-system-card) (2026-04-23)
- ...

## 个人 Blog
- ...

## 新论文 — 关注作者
- **arXiv (Yann LeCun)** — [Title](https://arxiv.org/abs/...) — Yann LeCun, ... (2026-05-02)

## 新论文 — 关键词命中
- ...
```

VS Code、Obsidian、`bat` 等都能直接读。

推荐用 Obsidian 把 `reports/` 目录设为 vault，标签 + 双链就能积累自己的 AI 阅读笔记。

## 6. 故障排查

### 日报是空的

正常情况下两种可能：

1. **首次 init 后第一次 run** — 设计如此，所有当前条目都已 mark seen。明天会有增量。
2. **真的没新内容** — 跑 `verify` 看每个源最新条目，对比 `data/seen.sqlite`：

   ```bash
   .venv/bin/python -c "
   import sqlite3
   c = sqlite3.connect('data/seen.sqlite')
   for row in c.execute('SELECT source, COUNT(*) FROM seen GROUP BY source ORDER BY 2 DESC'):
       print(row)
   "
   ```

### 某个源失效

日报顶部会有：

```
> ⚠️ Source errors: Anthropic: ...
```

跑 `verify` 看具体错误。常见两种：

- **HTTP 4xx/5xx**：站点改版或临时挂了，等一天再看
- **EMPTY**（HTML 源）：选择器失效。打开 `src/aidigest/fetchers/html.py` 的 `_extract_title` 或改 `sources.yaml` 的 `link_pattern`

### 重置一切

```bash
rm data/seen.sqlite
PYTHONPATH=src .venv/bin/python -m aidigest init
```

之后第一次 `run` 又会是空的，从下一次开始有增量。

### launchd 没在跑

```bash
# 检查是否加载
launchctl list | grep aidigest

# 看错误日志
cat logs/launchd.err.log

# 看应用日志
tail -50 logs/aidigest.log

# 手动验证脚本本身能跑
./scripts/run.sh
```

最常见原因：plist 里的路径有 typo，或者 `.venv` 不存在。

## 7. 日常使用建议

- **早上喝咖啡时扫一眼今天的日报**，3-5 分钟
- 看到感兴趣的就点链接进原文
- 一周一次清理 `reports/`：保留有过笔记的，删除空翻过的（或者 `git add reports/ && git commit` 全留着，反正都是文本）
- 每月看一次 `keywords` 命中质量，调词表
- 出差/休假回来，前面几天的日报会堆着，可以一次性扫，或直接 `rm reports/<old-date>.md`

## 8. 常用速查

| 想做 | 命令 |
|---|---|
| 跑一次 | `./scripts/run.sh` |
| 测源 | `PYTHONPATH=src .venv/bin/python -m aidigest verify` |
| 重置 seen | `rm data/seen.sqlite && PYTHONPATH=src .venv/bin/python -m aidigest init` |
| 看今天日报 | `open reports/$(date +%F).md` |
| 暂停自动跑 | `launchctl unload ~/Library/LaunchAgents/com.zw.aidigest.plist` |
| 恢复自动跑 | `launchctl load ~/Library/LaunchAgents/com.zw.aidigest.plist` |
