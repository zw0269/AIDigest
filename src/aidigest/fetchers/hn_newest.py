import logging
import re

import httpx
from selectolax.parser import HTMLParser

from ..models import Item


log = logging.getLogger(__name__)

_USER_AGENT = "Mozilla/5.0 (compatible; AIDigest/0.1)"
_BASE_URL = "https://news.ycombinator.com/newest"
_ITEM_URL = "https://news.ycombinator.com/item?id={}"

# HN 上常见的占位/测试帖噪音，按精确标题（大小写不敏感、去首尾空白）过滤掉。
_TITLE_BLACKLIST = re.compile(r"^(?:poll:\s*)?test$", re.IGNORECASE)


def fetch(source_name: str, url: str = _BASE_URL, category: str = "community") -> list[Item]:
    try:
        resp = httpx.get(
            url,
            headers={"User-Agent": _USER_AGENT},
            follow_redirects=True,
            timeout=30.0,
        )
        resp.raise_for_status()
    except httpx.HTTPError as e:
        log.warning("HN newest fetch failed (%s): %s", url, e)
        return []

    tree = HTMLParser(resp.text)
    items: list[Item] = []

    for row in tree.css("tr.athing"):
        story_id = row.attributes.get("id") or ""
        if not story_id:
            continue
        a = row.css_first("span.titleline a")
        if not a:
            continue
        title = " ".join(a.text(strip=True).split())
        if not title:
            continue
        if _TITLE_BLACKLIST.match(title):
            continue
        canonical_url = _ITEM_URL.format(story_id)
        items.append(
            Item(
                id=f"hn:{story_id}",
                title=title,
                url=canonical_url,
                source=source_name,
                category=category,
                published=None,
            )
        )
    return items
