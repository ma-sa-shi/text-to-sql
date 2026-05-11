#### ordersテーブル

| カラム名 | 型 | 制約 | デフォルト | 論理名・説明 |
| --- | --- | --- | --- | --- |
| order_id | INT | PK, AUTO_INCREMENT | - | 注文ID |
| user_id | INT | NOT NULL, FK | - | ユーザーID |
| order_number | VARCHAR(50) | NOT NULL, UNIQUE | - | 注文番号 |
| order_status | ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled', 'refunded') | - | 'pending' | 注文ステータス |
| total_amount | DECIMAL(15, 2) | NOT NULL | - | 合計金額 |
| tax_amount | DECIMAL(12, 2) | NOT NULL | - | 税額 |
| shipping_fee | DECIMAL(10, 2) | - | 0.00 | 送料 |
| discount_amount | DECIMAL(10, 2) | - | 0.00 | 割引額 |
| payment_method | ENUM('credit_card', 'paypal', 'bank_transfer', 'cod') | - | NULL | 支払い方法 |
| shipping_address_line1 | VARCHAR(255) | NOT NULL | - | 配送先住所1 |
| shipping_address_line2 | VARCHAR(255) | - | NULL | 配送先住所2 |
| city | VARCHAR(100) | - | NULL | 市区町村 |
| state_province | VARCHAR(100) | - | NULL | 都道府県・州 |
| postal_code | VARCHAR(20) | - | NULL | 郵便番号 |
| country_code | CHAR(2) | - | NULL | 国コード |
| tracking_number | VARCHAR(100) | - | NULL | 追跡番号 |
| ordered_at | TIMESTAMP | - | CURRENT_TIMESTAMP | 注文日時 |
| shipped_at | DATETIME | - | NULL | 出荷日時 |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
