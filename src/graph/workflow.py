from langgraph.graph import StateGraph, END
from share.schema import GraphState
from graph.nodes import (
    generate_queries_node,
    retrieve_and_filter_tables_node,
    generate_sql_node,
    execute_sql_node,
    interpret_sql_result_node,
)

workflow = StateGraph(GraphState)
workflow.add_node("query_gen", generate_queries_node)
workflow.add_node("retrieve_and_filter_tables", retrieve_and_filter_tables_node)
workflow.add_node("generate_sql", generate_sql_node)
workflow.add_node("execute_sql", execute_sql_node)
workflow.add_node("interpret_sql_result", interpret_sql_result_node)

workflow.set_entry_point("query_gen")

workflow.add_edge("query_gen", "retrieve_and_filter_tables")
workflow.add_edge("retrieve_and_filter_tables", "generate_sql")
workflow.add_edge("generate_sql", "execute_sql")
workflow.add_edge("execute_sql", "interpret_sql_result")
workflow.add_edge("interpret_sql_result", END)

compiled = workflow.compile()
