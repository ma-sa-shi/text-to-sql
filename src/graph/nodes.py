from share.schema import GraphState
from share.vectorstore import retrieve_tables
from share.utils import (
    flatten_documents,
    get_unique_documents,
    refilter_with_cohere,
    get_context,
)
from share.database import execute
from graph.chains import (
    generate_queries_chain,
    generate_sql_chain,
    interpret_sql_result_chain,
    generate_failure_response_chain,
)


def generate_queries_node(state: GraphState) -> dict:
    """質問からクエリを生成するノード"""
    queries = generate_queries_chain.invoke({"question": state.get("question")})
    return {"queries": queries}


def retrieve_and_filter_tables_node(state: GraphState) -> dict:
    """クエリからテーブルを検索し、Cohereでrerankして更に絞り込みテーブルの詳細情報を取得するノード"""
    question = state.get("question")
    queries = state.get("queries")

    # ベクトル検索 (nested_docs: list[list[Document]])
    nested_docs = retrieve_tables(queries)

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


def generate_sql_node(state: GraphState) -> dict:
    """テーブル詳細情報からSQLを生成するノード"""
    question = state.get("question")
    selected_table_schemas = "\n\n".join(state.get("selected_table_schemas"))
    error_message = state.get("error_message")
    generated_sql = state.get("generated_sql")

    generated_sql = generate_sql_chain.invoke(
        {
            "question": question,
            "selected_table_schemas": selected_table_schemas,
            "error_message": error_message,
            "generated_sql": generated_sql,
        }
    )
    return {"generated_sql": generated_sql}


def execute_sql_node(state: GraphState) -> dict:
    """SQLを実行するノード"""
    generated_sql = state.get("generated_sql")
    result = execute(generated_sql)

    if result.get("error"):
        return {
            "error_message": result.get("error"),
            "retry_count": state.get("retry_count", 0) + 1,
        }

    return {"execution_result": result.get("result")}


def interpret_sql_result_node(state: GraphState) -> dict:
    """SQL実行結果から回答を生成するノード"""
    question = state.get("question")
    execution_result = state.get("execution_result")
    final_answer = interpret_sql_result_chain.invoke(
        {"question": question, "result": execution_result}
    )
    return {"final_answer": final_answer}


def generate_failure_response_node(state: GraphState) -> dict:
    """SQL実行結果から失敗理由を生成するノード"""
    question = state.get("question")
    generated_sql = state.get("generated_sql")
    error_message = state.get("error_message")
    final_answer = generate_failure_response_chain.invoke(
        {
            "question": question,
            "generated_sql": generated_sql,
            "error_message": error_message,
        }
    )
    return {"final_answer": final_answer}
