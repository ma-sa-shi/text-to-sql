#### wishlistsテーブル

| カラム名 | 型 | 制約 | デフォルト | 説明 |
| --- | --- | --- | --- | --- |
| wishlist_id | INT | PK, AUTO_INCREMENT | - | wishlist ID |
| user_id | INT | NOT NULL, FK | - | ユーザーID |
| product_id | INT | NOT NULL, FK | - | 商品ID |
| added_at | TIMESTAMP | - | CURRENT_TIMESTAMP | 追加日時 |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
