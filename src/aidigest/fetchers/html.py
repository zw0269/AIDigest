import logging
import re
from urllib.parse import urljoin

import httpx
from selectolax.parser import HTMLParser, Node

from ..dedupe import canonical_id
from ..models import Item


log = logging.getLogger(__name__)

_USER_AGENT = "Mozilla/5.0 (compatible; AIDigest/0.1)"
_DATE_PATTERNS = [
    re.compile(r"^[A-Z][a-z]{2}\s+\d{1,2},\s+\d{4}$"),
    re.compile(r"^\d{4}-\d{2}-\d{2}$"),
]


def _extract_title(anchor: Node) -> str:
    for tag in ("h1", "h2", "h3", "h4"):
        node = anchor.css_first(tag)
        if node:
            text = node.text(strip=True)
            if text:
                return text

    for span in anchor.css("span"):
        cls = span.attributes.get("class", "") or ""
        if "title" in cls.lower():
            text = span.text(strip=True)
            if text:
                return text

    raw = anchor.text(separator=" ", strip=True)
    parts = [p.strip() for p in re.split(r"\s{2,}|\n+", raw) if p.strip()]
    parts = [p for p in parts if not any(rx.match(p) for rx in _DATE_PATTERNS)]
    parts = [p for p in parts if p.lower() not in {"product", "announcements", "society", "policy", "research"}]
    return max(parts, key=len) if parts else raw[:200]


def fetch(source_name: str, url: str, link_pattern: str, category: str) -> list[Item]:
    pattern = re.compile(link_pattern)
    try:
        resp = httpx.get(
            url,
            headers={"User-Agent": _USER_AGENT},
            follow_redirects=True,
            timeout=30.0,
        )
        resp.raise_for_status()
    except httpx.HTTPError as e:
        log.warning("HTML fetch failed for %s (%s): %s", source_name, url, e)
        return []

    tree = HTMLParser(resp.text)
    items: list[Item] = []
    seen_urls: set[str] = set()

    for a in tree.css("a"):
        href = a.attributes.get("href") or ""
        if not pattern.search(href):
            continue
        full_url = urljoin(url, href)
        if full_url in seen_urls:
            continue
        seen_urls.add(full_url)

        title = _extract_title(a)
        if not title:
            continue

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
