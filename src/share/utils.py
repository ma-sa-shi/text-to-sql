from pathlib import Path
from langchain_core.documents import Document


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
    unique_docs = {doc.metadata.table_name: doc for doc in documents}
    return list(unique_docs.values())
