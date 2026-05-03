import logging
from datetime import datetime, timedelta

import feedparser

from ..dedupe import canonical_id
from ..models import Item


log = logging.getLogger(__name__)


def fetch(source_name: str, url: str, category: str, lookback_days: int | None = None) -> list[Item]:
    feed = feedparser.parse(url)
    if feed.bozo and not feed.entries:
        log.warning("RSS parse failed for %s (%s): %s", source_name, url, feed.bozo_exception)
        return []

    cutoff = datetime.now() - timedelta(days=lookback_days) if lookback_days else None
    items: list[Item] = []
    for entry in feed.entries:
        link = getattr(entry, "link", None)
        title = getattr(entry, "title", None)
        if not link or not title:
            continue

        published = None
        for attr in ("published_parsed", "updated_parsed"):
            t = getattr(entry, attr, None)
            if t:
                try:
                    published = datetime(*t[:6])
                except (TypeError, ValueError):
                    pass
                break

        if cutoff and published and published < cutoff:
            continue

        items.append(
            Item(
                id=canonical_id(link),
                title=title.strip(),
                url=link,
                source=source_name,
                category=category,
                published=published,
            )
        )
    return items
