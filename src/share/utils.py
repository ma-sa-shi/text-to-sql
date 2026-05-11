def parse_md_to_records(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return

    lines = md_content.strip().split("\n")

    data_lines = [line for line in lines if "|" in line and "---" not in line][1:]

    records = []

    for line in data_lines:
        columns = [col.strip() for col in line.strip("|").split("|")]

        if len(columns) >= 3:
            physical_name = columns[0]
            logical_name = columns[1]
            description = columns[2]

            records.append(
                {
                    "table_name": physical_name,
                    "logical_name": logical_name,
                    "description": description,
                    "embedding_text": f"テーブル物理名: {physical_name}, 論理名: {logical_name}, 概要: {description}",
                }
            )
    return records
