import logging
from datetime import datetime, timedelta, timezone

import arxiv

from ..dedupe import canonical_id
from ..models import Item


log = logging.getLogger(__name__)

_client = arxiv.Client(page_size=50, delay_seconds=3, num_retries=3)


def _recent_cutoff(lookback_days: int) -> datetime:
    return datetime.now(timezone.utc) - timedelta(days=lookback_days)


def _to_item(result: arxiv.Result, source: str, category: str) -> Item:
    return Item(
        id=canonical_id(result.entry_id),
        title=result.title.strip().replace("\n", " "),
        url=result.entry_id,
        source=source,
        category=category,
        published=result.published,
        authors=[a.name for a in result.authors],
    )


def fetch_by_keywords(
    categories: list[str],
    keywords: list[str],
    max_results: int,
    lookback_days: int,
) -> list[Item]:
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    kw_query = " OR ".join(f'all:"{k}"' for k in keywords)
    query = f"({cat_query}) AND ({kw_query})"

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    cutoff = _recent_cutoff(lookback_days)
    items: list[Item] = []
    try:
        for result in _client.results(search):
            if result.published < cutoff:
                break
            items.append(_to_item(result, "arXiv (keyword)", "arxiv-keyword"))
    except Exception as e:
        log.warning("arXiv keyword search failed: %s", e)
    return items


def fetch_by_authors(
    authors: list[str],
    max_results_per_author: int,
    lookback_days: int,
) -> list[Item]:
    cutoff = _recent_cutoff(lookback_days)
    items: list[Item] = []
    for author in authors:
        query = f'au:"{author}"'
        search = arxiv.Search(
            query=query,
            max_results=max_results_per_author,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        try:
            for result in _client.results(search):
                if result.published < cutoff:
                    break
                items.append(_to_item(result, f"arXiv ({author})", "arxiv-author"))
        except Exception as e:
            log.warning("arXiv author search failed for %s: %s", author, e)
    return items
