import os
from os.path import join, dirname
from dotenv import load_dotenv


class Settings:
    APP_ENVIRONMENT: str = None
    SECRET_KEY: str = None
    PORT: int = None
    DATABASE_URI: str = None
    API_URL: str = None
    ALGORITHM: str = None
    ACCESS_TOKEN_EXPIRE_MINUTES: int = None

    @classmethod
    def load_config(cls):
        dotenv_path = join(dirname(__file__), '../../.env')
        load_dotenv(dotenv_path)

        cls.APP_ENVIRONMENT = os.environ.get('ENVIRONMENT')
        cls.SECRET_KEY = os.environ.get('APP_SECRET')
        cls.PORT = int(os.environ.get('PORT'))
        cls.API_URL = os.environ.get('API_URL')

        cls.ALGORITHM = os.environ.get('ALGORITHM')
        cls.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES'))

        if cls.APP_ENVIRONMENT == 'development':
            cls.DATABASE_URI = os.environ.get("DATABASE_URI")

        if cls.APP_ENVIRONMENT == 'production':
            cls.DATABASE_URI = os.environ.get("PRODUCTION_DATABASE_URI")

        if cls.APP_ENVIRONMENT == 'test':
            cls.DATABASE_URI = os.environ.get("TEST_DATABASE_URI")

        return cls
