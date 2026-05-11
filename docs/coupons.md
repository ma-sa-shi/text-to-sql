#### couponsテーブル

| カラム名 | 型 | 制約 | デフォルト | 論理名・説明 |
| --- | --- | --- | --- | --- |
| coupon_id | INT | PK, AUTO_INCREMENT | - | クーポンID |
| coupon_code | VARCHAR(20) | NOT NULL, UNIQUE | - | クーポンコード |
| discount_type | ENUM('fixed', 'percentage') | NOT NULL | - | 割引種別（定額/定率） |
| discount_value | DECIMAL(10, 2) | NOT NULL | - | 割引額または割引率 |
| min_purchase_amount | DECIMAL(12, 2) | - | 0.00 | 最低購入金額 |
| max_discount_amount | DECIMAL(12, 2) | - | NULL | 最大割引限度額 |
| starts_at | DATETIME | - | NULL | 開始日時 |
| expires_at | DATETIME | - | NULL | 有効期限 |
| usage_limit | INT | - | NULL | 利用回数制限 |
| used_count | INT | - | 0 | 現在の利用回数 |
| is_active | BOOLEAN | - | TRUE | 有効フラグ |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
