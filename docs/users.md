#### usersテーブル

| カラム名 | 型 | 制約 | デフォルト | 説明 |
| --- | --- | --- | --- | --- |
| user_id | INT | PK, AUTO_INCREMENT | - | ユーザーID |
| username | VARCHAR(50) | NOT NULL, UNIQUE | - | ユーザー名（一意） |
| email | VARCHAR(100) | NOT NULL, UNIQUE | - | メールアドレス（一意） |
| password_hash | VARCHAR(255) | NOT NULL | - | パスワードハッシュ |
| first_name | VARCHAR(50) | - | NULL | 名 |
| last_name | VARCHAR(50) | - | NULL | 姓 |
| phone_number | VARCHAR(20) | - | NULL | 電話番号 |
| birth_date | DATE | - | NULL | 生年月日 |
| gender | ENUM('male', 'female', 'other', 'prefer_not_to_say') | - | NULL | 性別 |
| is_active | BOOLEAN | - | TRUE | 有効フラグ |
| membership_tier | ENUM('standard', 'silver', 'gold', 'platinum') | - | 'standard' | 会員ランク |
| last_login_at | DATETIME | - | NULL | 最終ログイン日時 |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
