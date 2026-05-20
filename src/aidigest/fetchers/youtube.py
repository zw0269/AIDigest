"""YouTube AI 视频 fetcher。

通过 yt-dlp 搜索关键词，URL 上挂 ``sp=EgIIAg``（YouTube 端「今日上传」筛选器），
合并去重后按播放量降序取 Top N。返回的 Item 走 community 分类。
"""

import logging
from urllib.parse import quote_plus

from yt_dlp import YoutubeDL

from ..models import Item


log = logging.getLogger(__name__)

# YouTube 搜索 URL：sp=EgIIAg 是「上传日期 = 今天」的过滤器编码
_SEARCH_URL = "https://www.youtube.com/results?search_query={q}&sp=EgIIAg"

# 默认关键词：用户选的「LLM/GPT/Claude/Gemini 强信号」
_DEFAULT_KEYWORDS = ["LLM", "GPT", "Claude", "Gemini"]


def fetch(
    source_name: str = "YouTube AI",
    keywords: list[str] | None = None,
    max_results: int = 5,
    per_keyword: int = 50,
    min_duration_seconds: int = 60,
    category: str = "community",
) -> list[Item]:
    kws = keywords or _DEFAULT_KEYWORDS
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "extract_flat": "in_playlist",
        "playlist_items": f"1-{per_keyword}",
    }

    candidates: dict[str, dict] = {}
    with YoutubeDL(ydl_opts) as ydl:
        for kw in kws:
            url = _SEARCH_URL.format(q=quote_plus(kw))
            try:
                result = ydl.extract_info(url, download=False)
            except Exception as e:
                log.warning("YouTube search failed for %r: %s", kw, e)
                continue
            for entry in (result.get("entries") or []):
                if not entry:
                    continue
                vid = entry.get("id")
                if not vid:
                    continue
                if entry.get("live_status") == "is_live":
                    continue
                duration = entry.get("duration") or 0
                if duration and duration < min_duration_seconds:
                    continue
                prev = candidates.get(vid)
                cur_views = entry.get("view_count") or 0
                if prev and (prev.get("view_count") or 0) >= cur_views:
                    continue
                candidates[vid] = entry

    ranked = sorted(
        candidates.values(),
        key=lambda e: e.get("view_count") or 0,
        reverse=True,
    )[:max_results]

    items: list[Item] = []
    for e in ranked:
        vid = e["id"]
        title = (e.get("title") or vid).strip()
        channel = (e.get("channel") or e.get("uploader") or "").strip()
        views = e.get("view_count") or 0
        head = f"{channel} — {title}" if channel else title
        full_title = f"{head}（{views:,} 次播放）"
        items.append(
            Item(
                id=f"yt:{vid}",
                title=full_title,
                url=f"https://www.youtube.com/watch?v={vid}",
                source=source_name,
                category=category,
            )
        )
    return items
