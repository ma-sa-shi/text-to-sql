import os
from pathlib import Path
from langchain_core.documents import Document
from langchain_cohere import CohereRerank


def flatten_documents(nested_documents: list[list[Document]]) -> list[Document]:
    """2次元配列のドキュメントリストを1次元に平坦化する関数。"""
    return [doc for sublist in nested_documents for doc in sublist]


def parse_md_to_records(file_path: str) -> list[dict]:
    """table_summaries.mdを辞書のリストに変換する関数。
    Args:
        file_path (str): table_summaries.mdのパス
    Returns:
        list[dict]: 辞書のリスト
    """
    path = Path(file_path)

    if not path.exists():
        print(f"ファイルが見つかりません: {file_path}")
        return

    md_content = path.read_text(encoding="utf-8")

    lines = md_content.strip().split("\n")

    data_lines = [line for line in lines if "|" in line and "---" not in line]

    records = []

    for line in data_lines:
        columns = [col.strip() for col in line.strip("|").split("|")]

        if len(columns) >= 3:
            physical_name = columns[0]
            logical_name = columns[1]
            description = columns[2]

            records.append(
                {
                    "table_name": physical_name,
                    "logical_name": logical_name,
                    "description": description,
                    "embedding_text": f"テーブル物理名: {physical_name}, 論理名: {logical_name}, 概要: {description}",
                }
            )
    return records


def get_unique_documents(documents: list[Document]) -> list[Document]:
    """重複無しのドキュメントのリストを返す関数。
    Args:
        documents (list[Document]): ドキュメントのリスト
    Returns:
        list[Document]: 重複のないドキュメントのリスト
    """
    unique_docs = {doc.metadata.get("table_name"): doc for doc in documents}
    return list(unique_docs.values())


def refilter_with_cohere(question: str, documents: list[Document]) -> list[str]:
    """cohereでrerankして5個のドキュメントに絞りテーブル名を返す関数。
    Args:
        question (str): ユーザーの質問
        documents (list[Document]): ドキュメントのリスト
    Returns:
        list[str]: テーブル名のリスト
    """
    cohere_reranker = CohereRerank(
        model=os.getenv("COHERE_MODEL_NAME", "rerank-v3.5"), top_n=5
    )
    selected_documents = cohere_reranker.compress_documents(
        documents=documents, query=question
    )
    selected_table = [doc.metadata.get("table_name") for doc in selected_documents]

    return selected_table


def get_context(selected_table: list[str]) -> list[str]:
    """テーブルの詳細情報を取得する関数。
    Args:
        selected_table (list[str]): テーブル名のリスト
    Returns:
        list[str]: テーブルの詳細情報のリスト
    """
    docs_dir = Path("docs")
    contexts = []
    for table in selected_table:
        table_file = docs_dir / f"{table}.md"

        try:
            content = table_file.read_text(encoding="utf-8")
            contexts.append(content)
        except FileNotFoundError:
            print(f"ファイルが見つかりません: {table_file}")
            contexts.append("")

    return contexts
