import os
import sqlite3
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DEFAULT_DB_PATH = os.path.join(PROJECT_ROOT, "spam_monitor.db")


def get_connection(db_path=DEFAULT_DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path=DEFAULT_DB_PATH):
    conn = get_connection(db_path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS inbox_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            prediction TEXT NOT NULL,
            confidence REAL NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def log_prediction(message, prediction, confidence, db_path=DEFAULT_DB_PATH):
    init_db(db_path)
    conn = get_connection(db_path)
    conn.execute(
        "INSERT INTO inbox_entries (message, prediction, confidence, created_at) VALUES (?, ?, ?, ?)",
        (message, prediction, float(confidence), datetime.utcnow().isoformat(timespec="seconds")),
    )
    conn.commit()
    conn.close()


def get_recent_messages(limit=10, db_path=DEFAULT_DB_PATH):
    init_db(db_path)
    conn = get_connection(db_path)
    rows = conn.execute(
        "SELECT message, prediction, confidence, created_at FROM inbox_entries ORDER BY id DESC LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
