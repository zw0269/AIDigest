"""GitHub 短描述补充工具（report-only 旁注，不进 digest）。

背景：GitHub Trending 抓到的描述就是仓库 About，偶尔极短或为空（如
`git push no-mistakes`），导致写中文摘要时只能臆测、容易出错。

本脚本扫描某天的 reports/YYYY-MM-DD.md，挑出 **描述短于 N 字（默认 30）**
的 GitHub Trending 条目，抓 README 正文摘录（拿不到再用 GitHub API 的
description 兑底），把结果写进 reports/YYYY-MM-DD.enrich.md 旁注，供 /scrape
第 2 步写 MANUAL_SUMMARIES 时参考。旁注落在 reports/（已 gitignore），不提交、
不进最终 digest。

用法：
    ./.venv/bin/python scripts/enrich_short_descs.py 2026-06-25 [--threshold 30]

可选环境变量 GITHUB_TOKEN：设置后抬高 GitHub API 速率上限（默认匿名 60/小时，
对每天个位数仓库足够）。
"""

import argparse
import os
import re
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"

# 复用 cli.py 的 bullet 解析口径：- **<source>** — [<text>](<url>)
_BULLET_RE = re.compile(r"^- \*\*([^*]+)\*\* — \[(.+?)\]\(([^)]+)\)")
_REPO_RE = re.compile(r"^https?://github\.com/([^/]+)/([^/#?]+)")


def _api_headers() -> dict[str, str]:
    headers = {"User-Agent": "AIDigest-enrich/0.1"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _readme_excerpt(md_text: str, limit: int = 700) -> str:
    """清洗 README 给出一段可读摘录（原始素材，供人/LLM 判断后写中文）。

    不试图精挑“第一句”——那对 HTML 排版、非英文、徽章开头的 README 太脆。
    改为去掉代码块/HTML 标签/徽章/图片/标题，收集前若干行正文，截到 limit 字符。
    """
    # 先在全文上做跨行清洗（HTML 标签/徽章常跨多行，逐行处理会漏）
    text = re.sub(r"```.*?```", " ", md_text, flags=re.S)  # 代码块
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)  # HTML 注释
    text = re.sub(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)", " ", text)  # 徽章链接
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)  # 图片
    text = re.sub(r"<[^>]+>", " ", text)  # HTML 标签（[^>] 含换行，可跨行匹配）

    out: list[str] = []
    total = 0
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):  # 跳过空行与标题
            continue
        line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)  # [文字](链接) -> 文字
        line = re.sub(r"^[>*\-\d.\s]+", "", line)  # 列表/引用前缀
        line = re.sub(r"[*_`]", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        # 真实字母/汉字少于 8 个的行（徽章残渣、符号行）丢弃
        if len(re.sub(r"[^0-9A-Za-zА-Яа-яЁё一-鿿]", "", line)) < 8:
            continue
        out.append(line)
        total += len(line)
        if total > limit:
            break
    return " ".join(out)[:limit]


# raw CDN 不受 GitHub API 60/小时 限流，优先走它取 README
_README_NAMES = ("README.md", "readme.md", "README.rst", "README", "README.markdown")


def _fetch_readme(owner: str, repo: str, client: httpx.Client) -> str:
    for fn in _README_NAMES:
        resp = client.get(f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/{fn}")
        if resp.status_code == 200 and resp.text.strip():
            excerpt = _readme_excerpt(resp.text)
            if excerpt:
                return excerpt
    return ""


def _fetch_description(owner: str, repo: str, client: httpx.Client) -> str:
    """API 兑底：拿仓库 About。403 限流时抛出，让调用方在旁注里点明。"""
    resp = client.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=_api_headers(),
    )
    if resp.status_code == 403 and "rate limit" in resp.text.lower():
        raise RuntimeError("GitHub API 限流 403（可设 GITHUB_TOKEN 后重试）")
    resp.raise_for_status()
    return (resp.json().get("description") or "").strip()


def _candidates(report: Path, threshold: int) -> list[tuple[str, str, str]]:
    """返回 (url, name, desc) 列表，仅 GitHub Trending 且 desc 短于 threshold。"""
    out: list[tuple[str, str, str]] = []
    for line in report.read_text().splitlines():
        m = _BULLET_RE.match(line.strip())
        if not m or m.group(1) != "GitHub Trending":
            continue
        url = m.group(3)
        text = m.group(2)
        name, _, desc = text.partition(" — ")
        if len(desc.strip()) < threshold:
            out.append((url, name.strip(), desc.strip()))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="补充 GitHub 短描述条目的真实链接内容")
    ap.add_argument("date", help="报告日期 YYYY-MM-DD")
    ap.add_argument("--threshold", type=int, default=30, help="描述短于该字符数才补充（默认 30）")
    args = ap.parse_args()

    report = REPORTS_DIR / f"{args.date}.md"
    if not report.exists():
        print(f"找不到报告：{report}", file=sys.stderr)
        return 1

    cands = _candidates(report, args.threshold)
    if not cands:
        print(f"{args.date}: 无短于 {args.threshold} 字的 GitHub 条目，跳过。")
        return 0

    blocks: list[str] = [f"# GitHub 短描述补充 — {args.date}\n"]
    with httpx.Client(follow_redirects=True, timeout=20.0) as client:
        for url, name, desc in cands:
            rm = _REPO_RE.match(url)
            if not rm:
                continue
            owner, repo = rm.group(1), rm.group(2)
            enriched, source, err = "", "", ""
            try:
                enriched = _fetch_readme(owner, repo, client)
                if enriched:
                    source = "README"
            except Exception as e:
                err = str(e)
            if not enriched:
                try:
                    enriched = _fetch_description(owner, repo, client)
                    if enriched:
                        source = "API description"
                except Exception as e:
                    err = str(e)
            note = enriched or f"（未取到内容：{err or '请手动核实'}）"
            blocks.append(
                f"## {name}\n"
                f"- URL: {url}\n"
                f"- 原描述: {desc or '（空）'}\n"
                f"- {source or '抓取失败'}: {note}\n"
            )
            print(f"  {name}: {source or '失败'} → {note[:80]}")

    out = REPORTS_DIR / f"{args.date}.enrich.md"
    out.write_text("\n".join(blocks) + "\n")
    print(f"\n写入旁注 {out}（{len(cands)} 条候选）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
