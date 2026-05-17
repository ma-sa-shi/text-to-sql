from share.schema import GraphState
from graph.chains import generate_queries_chain
from graph.utils import (
    search_tables_chain,
    flatten_documents,
    get_unique_documents,
    refilter_with_cohere,
    get_context,
)


def generate_queries_node(state: GraphState) -> dict:
    """質問からクエリを生成するノード"""
    queries = generate_queries_chain.invoke({"question": state.get("question")})
    return {"queries": queries}


def retrieve_and_filter_tables_node(state: GraphState) -> dict:
    """クエリからテーブルを検索し、Cohereでrerankして更に絞り込みテーブルの詳細情報を取得するノード"""
    question = state.get("question")
    queries = state("queries")

    # ベクトル検索 (nested_docs: list[list[Document]])
    nested_docs = search_tables_chain.invoke(queries)

    # 平坦化と重複排除
    flatten_docs = flatten_documents(nested_docs)
    unique_docs = get_unique_documents(flatten_docs)

    # Cohereによるセマンティック検索(selected_tables: list[str])
    selected_tables = refilter_with_cohere(question=question, documents=unique_docs)

    # テーブルの詳細情報の取得(selected_table_schemas: list[str])
    selected_table_schemas = get_context(selected_tables)

    return {
        "candidate_tables": unique_docs,
        "selected_table_schemas": selected_table_schemas,
    }
