from typing import Annotated, Any, TypedDict
import operator
from pydantic import BaseModel, Field


class MultiQuery(BaseModel):
    """LLMが生成する複数の検索クエリを表すクラス。
    Attributes:
        queries (list[str]): LLMが生成する検索クエリのリスト。3~5個のクエリが必要。
    """

    queries: list[str] = Field(
        ..., min_items=3, max_items=5, description="LLMが生成する検索クエリ"
    )


class GraphState(TypedDict):
    question: str
    queries: list[str]
    retrieved_summaries: list[dict[str, Any]]
    selected_schemas: list[dict[str, Any]]
    generated_sql: str
    error_history: Annotated[list[str], operator.add]
    execution_result: dict[str, Any]
    final_answer: str
    retry_count: int


"""
例)
retrieved_summaries = [
    {
        "text": "users",
        "table_name": ""
    },
]
selected_schemas = [
  {
    "table_name": "users",
    "logical_name": "顧客マスタ",
    "ddl": "CREATE TABLE orders (order_id INT, user_id INT, amount DECIMAL, order_date DATE)",
    "column_descriptions": [
        {"name": "status", "description": "0: 未入金, 1: 入金済, 9: キャンセル"}
    ],
  },
]

"""
