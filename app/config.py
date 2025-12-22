from functools import lru_cache
from typing import Dict, Type

from app.settings.base import BaseAppSettings, EnvSettings, AppEnvTypes
from app.settings.dev import DevAppSettings
from app.settings.test import TestAppSettings


environments: Dict[AppEnvTypes, Type[BaseAppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@lru_cache
def get_settings() -> BaseAppSettings:
    app_env = EnvSettings().ENV
    config = environments[app_env]
    return config()


settings = get_settings()
