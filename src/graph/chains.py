import os
from share.schema import MultiQuery
from graph.prompts import query_gen_prompt, generate_sql_prompt, interpret_sql_result
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


model = ChatOpenAI(model=os.getenv("OPENAI_MODEL_NAME", "gpt-5-nano"))

generate_queries_chain = (
    query_gen_prompt | model.with_structured_output(MultiQuery) | (lambda x: x.queries)
)

generate_sql_chain = generate_sql_prompt | model | StrOutputParser()

interpret_sql_result_chain = interpret_sql_result | model | StrOutputParser()
