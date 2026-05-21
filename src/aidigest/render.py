from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import Item


def render_report(
    items: list[Item],
    template_dir: Path,
    errors: list[str],
) -> str:
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(disabled_extensions=("md", "j2")),
    )
    tmpl = env.get_template("report.md.j2")

    companies = [i for i in items if i.category == "company"]
    individuals = [i for i in items if i.category == "individual"]
    community = [i for i in items if i.category == "community"]
    arxiv_authors = [i for i in items if i.category == "arxiv-author"]
    arxiv_keywords = [i for i in items if i.category == "arxiv-keyword"]

    def _sort_key(item: Item) -> datetime:
        pub = item.published
        if pub is None:
            return datetime.min
        # arXiv 给的是 tz-aware，RSS / 解析旧报告是 naive，混在同一桶里直接比较会 TypeError
        return pub.replace(tzinfo=None) if pub.tzinfo else pub

    for bucket in (companies, individuals, community, arxiv_authors, arxiv_keywords):
        bucket.sort(key=_sort_key, reverse=True)

    return tmpl.render(
        date=datetime.now().strftime("%Y-%m-%d"),
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M"),
        companies=companies,
        individuals=individuals,
        community=community,
        arxiv_authors=arxiv_authors,
        arxiv_keywords=arxiv_keywords,
        errors=errors,
        has_any=bool(items),
        total=len(items),
    )
