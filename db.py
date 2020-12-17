from tortoise.contrib.fastapi import register_tortoise


def init_db(config, app):
    register_tortoise(
        app,
        db_url=config.DATABASE_URI,
        modules={"models": ["src.models"]},
        generate_schemas=True,
        add_exception_handlers=True
    )
