#### inventory_logsテーブル

| カラム名 | 型 | 制約 | デフォルト | 論理名・説明 |
| --- | --- | --- | --- | --- |
| log_id | INT | PK, AUTO_INCREMENT | - | ログID |
| product_id | INT | NOT NULL, FK | - | 商品ID |
| variant_id | INT | FK | NULL | バリアントID |
| change_amount | INT | NOT NULL | - | 在庫変動量（正負の整数） |
| reason | ENUM('restock', 'sale', 'return', 'adjustment', 'damage') | NOT NULL | - | 変動理由 |
| notes | VARCHAR(255) | - | NULL | 備考 |
| created_by_user_id | INT | - | NULL | 作成者ユーザーID |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
