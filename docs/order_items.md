#### order_itemsテーブル

| カラム名 | 型 | 制約 | デフォルト | 論理名・説明 |
| --- | --- | --- | --- | --- |
| order_item_id | INT | PK, AUTO_INCREMENT | - | 注文明細ID |
| order_id | INT | NOT NULL, FK | - | 注文ID |
| product_id | INT | NOT NULL, FK | - | 商品ID |
| variant_id | INT | FK | NULL | バリアントID |
| quantity | INT | NOT NULL | - | 数量 |
| unit_price | DECIMAL(12, 2) | NOT NULL | - | 販売単価 |
| total_price | DECIMAL(15, 2) | GENERATED ALWAYS | - | 小計（数量×単価、自動計算） |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
