import logging
from urllib.parse import urljoin

import httpx
from selectolax.parser import HTMLParser

from ..dedupe import canonical_id
from ..models import Item


log = logging.getLogger(__name__)

_USER_AGENT = "Mozilla/5.0 (compatible; AIDigest/0.1)"
_BASE_URL = "https://github.com/trending"


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
        log.warning("GitHub trending fetch failed (%s): %s", url, e)
        return []

    tree = HTMLParser(resp.text)
    items: list[Item] = []
    seen: set[str] = set()

    for art in tree.css("article.Box-row"):
        a = art.css_first("h2 a")
        if not a:
            continue
        href = a.attributes.get("href") or ""
        full_url = urljoin(url, href)
        if full_url in seen:
            continue
        seen.add(full_url)

        name = " ".join(a.text(strip=True).split())
        desc_node = art.css_first("p")
        desc = " ".join(desc_node.text(strip=True).split()) if desc_node else ""
        title = f"{name} — {desc}" if desc else name

        items.append(
            Item(
                id=canonical_id(full_url),
                title=title,
                url=full_url,
                source=source_name,
                category=category,
                published=None,
            )
        )
    return items
