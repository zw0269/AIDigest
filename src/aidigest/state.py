import sqlite3
from pathlib import Path


class State:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS seen (
                id TEXT PRIMARY KEY,
                source TEXT NOT NULL,
                first_seen TEXT NOT NULL DEFAULT (datetime('now'))
            )
            """
        )
        self.conn.commit()

    def is_seen(self, item_id: str) -> bool:
        cur = self.conn.execute("SELECT 1 FROM seen WHERE id = ?", (item_id,))
        return cur.fetchone() is not None

    def mark_seen(self, item_id: str, source: str) -> None:
        self.conn.execute(
            "INSERT OR IGNORE INTO seen (id, source) VALUES (?, ?)",
            (item_id, source),
        )
        self.conn.commit()

    def mark_many(self, ids_with_source: list[tuple[str, str]]) -> None:
        self.conn.executemany(
            "INSERT OR IGNORE INTO seen (id, source) VALUES (?, ?)",
            ids_with_source,
        )
        self.conn.commit()

    def count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM seen").fetchone()[0]

    def close(self) -> None:
        self.conn.close()
