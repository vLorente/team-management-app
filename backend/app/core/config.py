from pathlib import Path
from typing import Any, List, Optional
from pydantic import AnyHttpUrl, EmailStr, PostgresDsn, validator
from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = Path(__file__).parent.parent / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Project
    PROJECT_NAME: str
    PROJECT_VERSION: str
    CORS_ORIGINS: List[AnyHttpUrl] = []

    # PostgreSQL
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    DATABASE_URI: Optional[PostgresDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values) -> Any:
        print(f'VALUES -> {values}')
        if isinstance(v, str):
            return v
        var = PostgresDsn.build(
            scheme="postgresql",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=values.get("POSTGRES_DB") or ''
        )
        print(f'URI -> {var}')
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=values.get("POSTGRES_DB") or ''
        )

    # Initial Data
    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str


settings = Settings(_env_file=env_path, _env_file_encoding='utf-8')
