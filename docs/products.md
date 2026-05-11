#### productsテーブル

| カラム名 | 型 | 制約 | デフォルト | 説明 |
| --- | --- | --- | --- | --- |
| product_id | INT | PK, AUTO_INCREMENT | - | 商品ID |
| category_id | INT | FK | NULL | カテゴリID |
| product_name | VARCHAR(255) | NOT NULL | - | 商品名 |
| sku | VARCHAR(100) | NOT NULL, UNIQUE | - | SKU（在庫管理単位） |
| short_description | VARCHAR(500) | - | NULL | 簡易説明 |
| full_description | LONGTEXT | - | NULL | 詳細説明 |
| base_price | DECIMAL(12, 2) | NOT NULL | - | 基本価格 |
| sale_price | DECIMAL(12, 2) | - | NULL | セール価格 |
| stock_quantity | INT | - | 0 | 在庫数 |
| weight_kg | DECIMAL(8, 2) | - | NULL | 重量(kg) |
| dimensions_cm | VARCHAR(50) | - | NULL | サイズ(cm) |
| is_featured | BOOLEAN | - | FALSE | おすすめフラグ |
| status | ENUM('draft', 'published', 'out_of_stock', 'discontinued') | - | 'draft' | ステータス |
| view_count | INT | - | 0 | 閲覧数 |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
