from langchain_core.prompts import ChatPromptTemplate

query_gen_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "ユーザーの質問を解決するために有効な検索クエリを3〜5個生成して",
        ),
        ("human", "質問: {question}"),
    ]
)

query_sql_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "テーブル情報を参照して質問が求めるデータを取得するSQLを生成して"),
        ("human", "質問: {question}\n\nテーブル情報: {selected_table_schemas}"),
    ]
)
