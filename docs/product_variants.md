#### product_variantsテーブル

| カラム名 | 型 | 制約 | デフォルト | 論理名・説明 |
| --- | --- | --- | --- | --- |
| variant_id | INT | PK, AUTO_INCREMENT | - | バリアントID |
| product_id | INT | NOT NULL, FK | - | 商品ID |
| variant_name | VARCHAR(100) | - | NULL | バリアント名（サイズ・カラー等） |
| sku_suffix | VARCHAR(50) | UNIQUE | NULL | SKUサフィックス |
| additional_price | DECIMAL(10, 2) | - | 0.00 | 追加価格 |
| stock_quantity | INT | - | 0 | 在庫数 |
| image_url | VARCHAR(255) | - | NULL | バリアント画像URL |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
