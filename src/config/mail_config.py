import os
from fastapi_mail import ConnectionConfig
from .settings import Settings

settings = Settings.load_config()

MAIL_CONFIG = ConnectionConfig(
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD"),
    MAIL_FROM=os.environ.get("MAIL_FROM"),
    MAIL_PORT=int(os.environ.get("MAIL_PORT")),
    MAIL_SERVER=os.environ.get("MAIL_SERVER"),
    MAIL_FROM_NAME=os.environ.get("MAIL_FROM_NAME"),
    MAIL_TLS=os.environ.get("MAIL_TLS"),
    MAIL_SSL=os.environ.get("MAIL_SSL"),
    USE_CREDENTIALS=os.environ.get("USE_CREDENTIALS")
)
