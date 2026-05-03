from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Item:
    id: str
    title: str
    url: str
    source: str
    category: str
    published: Optional[datetime] = None
    authors: list[str] = field(default_factory=list)
