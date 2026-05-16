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
    """ワークフローの状態を表すクラス。
    Attributes:
        question (str): ユーザーの質問
        queries (list[str]): LLMが生成する検索クエリのリスト
        candidate_tables(list[str]): ベクトル検索後の候補テーブルリスト
        selected_table_schemas (list[dict[str, Any]]): 抽出されたテーブル名と詳細情報のmdファイルの文字列の辞書のリスト
        generated_sql (str): LLMが生成したSQL
        error_history (list[str]): エラー履歴
        execution_result (dict[str, Any]): SQLの実行結果
        final_answer (str): ユーザーに渡す回答
        retry_count (int): リトライ回数
    """

    question: str
    queries: list[str]
    candidate_tables: list[str]
    selected_table_schemas: list[dict[str, Any]]
    generated_sql: str
    error_history: Annotated[list[str], operator.add]
    execution_result: dict[str, Any]
    final_answer: str
    retry_count: int
