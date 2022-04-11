from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: int = 8080
    db_url: str = "postgresql://hostman:b9392b97@94.228.113.90:5434/database"


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8",
)
