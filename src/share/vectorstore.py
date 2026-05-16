import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


def save_records_to_chroma(records, collection_name):
    PERSIST_DIRECTORY = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")
    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_EMBEDDING_MODEL_NAME", "text-embedding-3-small")
    )
    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY,
    )

    documents = [recode.get("embedding_text") for recode in records]
    metadatas = [
        {
            "table_name": record.get("table_name"),
            "logical_name": record.get("logical_name"),
            "description": record.get("description"),
        }
        for record in records
    ]

    ids = [record.get("table_name") for record in records]

    vectorstore.add_texts(documents=documents, metadatas=metadatas, ids=ids)

    return f"{len(ids)}件のテーブルを{collection_name}に保存しました。"


def get_retriever(k: int = 20):
    """ベクトルストアからドキュメントを検索するためのリトリーバーを取得する関数。
    Args:
        k (int): 検索するドキュメントの数
    Returns:
        VectorStoreRetriever: リトリーバー
    """
    PERSIST_DIRECTORY = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")

    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_EMBEDDING_MODEL_NAME", "text-embedding-3-small")
    )

    vectorstore = Chroma(
        persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings
    )
    return vectorstore.as_retriever(search_kwargs={"k": k})


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
