import os
import logging

from functools import lru_cache
from pydantic import BaseSettings
from pydantic.networks import AnyUrl


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info(
        "Loading config settings from environment ..............."
    )
    return Settings()
