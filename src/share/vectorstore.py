from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from share.config import settings


def get_vectorstore() -> Chroma:
    """共通設定のChromaベクトルストアを取得する関数。
    collection_nameはDB内のコレクション名(RDBのテーブルに相当)
    Returns:
        Chroma: ベクトルストア
    """
    embeddings = OpenAIEmbeddings(model=settings.openai_embedding_model_name)
    return Chroma(
        collection_name=settings.chroma_collection_name,
        embedding_function=embeddings,
        persist_directory=settings.chroma_persist_directory,
    )


def save_records_to_chroma(records: list[dict]) -> str:
    """テーブル概要のレコードをChromaに保存する関数。
    Args:
        records (list[dict]): parse_md_to_recordsで生成したレコードのリスト
    Returns:
        str: 保存結果のメッセージ
    """
    vectorstore = get_vectorstore()

    texts = [record.get("embedding_text") for record in records]
    metadatas = [
        {
            "table_name": record.get("table_name"),
            "logical_name": record.get("logical_name"),
            "description": record.get("description"),
        }
        for record in records
    ]

    ids = [record.get("table_name") for record in records]

    vectorstore.add_texts(texts=texts, metadatas=metadatas, ids=ids)

    return f"{len(ids)}件のテーブルを{settings.chroma_collection_name}に保存しました。"


def get_retriever():
    """ベクトルストアからドキュメントを検索するためのリトリーバーを取得する関数。
    Returns:
        VectorStoreRetriever: リトリーバー
    """
    return get_vectorstore().as_retriever(search_kwargs={"k": settings.chroma_search_k})


def retrieve_tables(queries: list[str]) -> list[Document]:
    """ベクトルストアからドキュメントを検索する関数。
    Args:
        queries (list[str]): 検索クエリのリスト
    Returns:
        list[str]: 検索結果のテーブル名のリスト
    """
    retriever = get_retriever()
    tables = retriever.map().invoke(queries)
    return tables
