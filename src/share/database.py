import sqlite3
import os
from typing import Any, TypedDict


class QueryResult(TypedDict):
    result: list[dict[str, Any]] | dict[str, int] | None
    error: str | None


def execute(sql: str) -> QueryResult:
    db_path = os.getenv("SQLITE_DB_PATH", "src/sql/application_tables.db")
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        # 辞書に変換できる型で行を返す
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql)
        is_select = sql.strip().upper().startswith("SELECT")

        if is_select:
            rows = cursor.fetchall()
            result = [dict(row) for row in rows]
        else:
            conn.commit()
            result = {"rowcount": cursor.rowcount}
        return {"result": result, "error": None}

    except sqlite3.Error as e:
        return {"result": None, "error": f"SQLite Error: {str(e)}"}

    finally:
        if conn:
            conn.close()
