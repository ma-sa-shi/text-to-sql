from langgraph.graph import StateGraph, END
from share.schema import GraphState
from graph.nodes import (
    generate_queries_node,
    retrieve_and_filter_tables_node,
    generate_sql_node,
    execute_sql_node,
    interpret_sql_result_node,
    generate_failure_response_node,
)


def decide_to_finish(state: GraphState):
    """SQL実行結果と再試行回数に基づいて、ワークフローの次のステップを決定する関数。
    Args:
        state (GraphState): 現在のグラフの状態
    Returns:
        str: 次のステップを示す文字列 ("finish", "force_finish", "retry")
    """
    if state.get("execution_result"):
        return "finish"

    if state.get("retry_count") >= 1:
        return "force_finish"

    return "retry"


workflow = StateGraph(GraphState)
workflow.add_node("query_gen", generate_queries_node)
workflow.add_node("retrieve_and_filter_tables", retrieve_and_filter_tables_node)
workflow.add_node("generate_sql", generate_sql_node)
workflow.add_node("execute_sql", execute_sql_node)
workflow.add_node("interpret_sql_result", interpret_sql_result_node)
workflow.add_node("generate_failure_response", generate_failure_response_node)

workflow.set_entry_point("query_gen")

workflow.add_edge("query_gen", "retrieve_and_filter_tables")
workflow.add_edge("retrieve_and_filter_tables", "generate_sql")
workflow.add_edge("generate_sql", "execute_sql")


workflow.add_conditional_edges(
    "execute_sql",
    decide_to_finish,
    {
        "finish": "interpret_sql_result",
        "force_finish": "generate_failure_response",
        "retry": "generate_sql",
    },
)

workflow.add_edge("interpret_sql_result", END)
workflow.add_edge("generate_failure_response", END)

compiled = workflow.compile()
