from config import Config

settings = Config.load_config()

# App db config
DB_CONFIG = {
        "connections": {"default": settings.DATABASE_URI},
        "apps": {
            "models": {
                "models": ["src.models"],
                "default_connection": "default"
            }
        }
    }
