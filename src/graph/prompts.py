from langchain_core.prompts import ChatPromptTemplate

query_gen_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ユーザーの質問を解決するために有効な検索クエリを3〜5個生成して"),
        ("human", "質問: {question}"),
    ]
)

generate_sql_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "テーブル情報を参照して質問が求めるデータを取得するSQLを生成して"
            "【注意事項】\n"
            "出力は解説やMarkdownの記号を含めず実行可能なSQLのみを出力すること\n"
            "「エラーメッセージ」と「実行したSQL」が提供されている場合は、「実行したSQL」に間違いがあることを意味する。「エラーメッセージ」から質問の意図を満たすように修正したSQLを生成して",
        ),
        (
            "human",
            "質問: {question}\n\nテーブル情報: {selected_table_schemas}\n\nエラーメッセージ: {error_message}\n\n実行したSQL: {generated_sql}",
        ),
    ]
)

interpret_sql_result = ChatPromptTemplate.from_messages(
    [
        ("system", "ユーザーの質問とSQL実行結果を基に質問に対する回答を生成して"),
        ("human", "質問: {question}\n\nSQL実行結果: {result}"),
    ]
)
