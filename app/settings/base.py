from enum import Enum
import os

from dotenv import load_dotenv
from pydantic import AnyUrl
from pydantic_settings import BaseSettings
from sqlalchemy import URL

load_dotenv()


class AppEnvTypes(str, Enum):
    dev = 'dev'
    test = 'test'
    production = 'production'


class EnvSettings(BaseSettings):
    ENV: AppEnvTypes = os.getenv("ENV", None) or AppEnvTypes.dev


class BaseAppSettings(EnvSettings):
    # General settings
    app_name: str = "Book store"
    debug: bool = False
    allowed_cors_origin: set[AnyUrl | str] = ["*"]
    allowed_cors_credentials: bool = True

    # DB settings
    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_PORT: int = os.getenv("DATABASE_PORT")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    DATABASE_URI: URL = URL.create(
        drivername="postgresql",
        username=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        database=DATABASE_NAME,
    )
