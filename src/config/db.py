from tortoise.contrib.fastapi import register_tortoise
from .db_config import DB_CONFIG


# Initialize db
def init_db(app):
    register_tortoise(
        app,
        config=DB_CONFIG,
        generate_schemas=True,
        add_exception_handlers=True,
    )

