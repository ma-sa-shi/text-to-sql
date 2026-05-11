#### product_reviewsテーブル

| カラム名 | 型 | 制約 | デフォルト | 論理名・説明 |
| --- | --- | --- | --- | --- |
| review_id | INT | PK, AUTO_INCREMENT | - | レビューID |
| product_id | INT | NOT NULL, FK | - | 商品ID |
| user_id | INT | NOT NULL, FK | - | ユーザーID |
| rating | TINYINT | CHECK (1-5) | - | 評価（星数） |
| title | VARCHAR(255) | - | NULL | レビュータイトル |
| comment | TEXT | - | NULL | レビュー本文 |
| is_verified_purchase | BOOLEAN | - | FALSE | 購入済み確認フラグ |
| helpful_votes | INT | - | 0 | 「役に立った」投票数 |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
