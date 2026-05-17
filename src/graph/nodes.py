from share.schema import GraphState
from graph.chains import generate_queries_chain


def generate_queries_node(state: GraphState):
    queries = generate_queries_chain.invoke({"question": state.get("question")})
    return {"queries": queries}
