import logging

from app.settings.base import BaseAppSettings


class TestAppSettings(BaseAppSettings):
    debug: bool = True
    log_level: int = logging.DEBUG
    site_host_url: str | None = None
