from pathlib import Path

from pydantic import BaseSettings


class API(BaseSettings):
    host: str
    port: int


class Settings(BaseSettings):
    api: API

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


def load_config(env_file=".env") -> Settings:
    BASE_DIR = Path(__file__).parent.parent
    settings = Settings(_env_file=BASE_DIR / env_file)
    return settings
