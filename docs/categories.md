#### categoriesテーブル

| カラム名 | 型 | 制約 | デフォルト | 論理名・説明 |
| --- | --- | --- | --- | --- |
| category_id | INT | PK, AUTO_INCREMENT | - | カテゴリID |
| parent_category_id | INT | FK | NULL | 親カテゴリID（自己参照） |
| category_name | VARCHAR(100) | NOT NULL | - | カテゴリ名 |
| description | TEXT | - | NULL | 説明文 |
| display_order | INT | - | 0 | 表示順 |
| is_visible | BOOLEAN | - | TRUE | 表示フラグ |
| slug | VARCHAR(100) | UNIQUE | NULL | スラッグ（URL用識別子） |
| is_deleted | BOOLEAN | - | FALSE | 論理削除フラグ |
| deleted_at | DATETIME | - | NULL | 論理削除日時 |
| created_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 作成日時 |
| updated_at | TIMESTAMP | NOT NULL | CURRENT_TIMESTAMP | 更新日時（ON UPDATE） |
