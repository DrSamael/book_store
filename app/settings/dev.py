from app.settings.base import BaseAppSettings


class DevAppSettings(BaseAppSettings):
    APP_NAME: str = "Dev Book store"
    DEBUG: bool = True
