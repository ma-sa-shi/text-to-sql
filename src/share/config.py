"""環境変数と共有パスの単一情報源（pydantic-settings版）。

全ての環境変数は.envで定義する（コード内にデフォルト値は持たない）。
不足がある場合はimport時に不足分をまとめてValidationErrorで報告する（fail fast）。
"""

from pathlib import Path

from pydantic import SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# 実行時のカレントディレクトリに依存しないよう、ファイル参照は__file__基準で解決する
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = PROJECT_ROOT / "docs"


class Settings(BaseSettings):
    """全フィールドにデフォルト値を持たせない

    - 実際の環境変数が.envより優先される（コンテナのenv_file注入と共存する）
    - 不足フィールドはValidationErrorで一括報告される
    - MYSQL_ROOT_PASSWORDなど未定義のキーはextra="ignore"で無視する
    """

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        frozen=True,
    )

    # APIキーはログに平文が出ないSecretStrで保持
    # 各SDKは環境変数から直接読むため、通常はここから取り出す必要はない
    openai_api_key: SecretStr
    cohere_api_key: SecretStr

    openai_model_name: str
    openai_embedding_model_name: str
    cohere_model_name: str

    mysql_host: str
    mysql_port: int
    mysql_user: str
    mysql_password: SecretStr
    mysql_database: str

    chroma_persist_directory: Path
    chroma_collection_name: str
    chroma_search_k: int
    cohere_rerank_top_n: int

    @field_validator(
        "openai_model_name",
        "openai_embedding_model_name",
        "cohere_model_name",
        "mysql_host",
        "mysql_user",
        "mysql_database",
        "chroma_collection_name",
        mode="before",
    )
    @classmethod
    def _reject_empty(cls, v: str) -> str:
        # 空文字列も未設定として扱う
        if isinstance(v, str) and not v.strip():
            raise ValueError("環境変数が空文字列です")
        return v


settings = Settings()
