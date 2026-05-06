# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Commit After Every Change

**Each completed code modification ends with a git commit.**

- After finishing a code change, run `git commit` to record it.
- Stage only the files related to the change; don't sweep in unrelated edits.
- Write a concise message describing the *why*, following the repo's existing commit style.
- If a pre-commit hook fails, fix the issue and create a new commit (don't `--amend` or `--no-verify`).
- Don't push unless explicitly asked.

## 6. 所有英文条目必须附中文注释（含论文）

**渲染日报中每个条目都必须有 `中文:` 行 — 包括 arXiv 论文。**

- **公司动态 / 个人 Blog（RSS）**：若 RSS 给出英文 description，必须在 `scripts/data.py` 的 `TRANSLATIONS` 中补上中文翻译/概括（一句话级别，不必逐字翻译）。
- **HTML 源（无 RSS description）**：在 `MANUAL_SUMMARIES` 中加中文摘要。
- **arXiv 论文**：标题虽是英文但 report 不带 abstract，必须用 `arxiv` 库按 ID 拉到 `summary` 后写一句中文核心要点，加进 `TRANSLATIONS`（key 为 `result.entry_id`，含 `v1` 后缀）。
- 仅有中文摘要的条目（Anthropic、Dario Amodei 等中文源）无需补英文。
- 渲染前必须抽查：`grep "中文:" llm-ai/digests/digest-YYYY-MM-DD.md | wc -l` 应等于当日条目总数；缺失先补再渲染，不要发只有英文/只有标题的 digest。

## 7. 抓取信息 = 跑 `/scrape`

当用户说"抓取信息"、"跑日报"、"更新 digest"或语义等价的请求时，按 `.claude/commands/scrape.md` 中的步骤执行：抓取 → 补中文 → 渲染 HTML → git commit。不要拆成手工命令一个个让用户确认。

## 8. 改信源或规则后必须重渲染 sources-and-rules.html

**`llm-ai/sources-and-rules.html` 是当前信源 / 规则的对外展示页，由 `scripts/build_sources_rules.py` 自动生成。**

- 改 `config/sources.yaml`（增删信源、调 arxiv 关键词/作者/lookback 等）后，必须跑 `./.venv/bin/python scripts/build_sources_rules.py` 重渲染。
- 改 CLAUDE.md（新增/修改/删除规则）后，同样必须重跑该脚本。
- 不要手工编辑 `sources-and-rules.html` — 它是产物。
- 渲染产物和源改动一起 commit，不要分两次提交导致页面短暂跟代码不一致。

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
