import uvicorn
from fastapi import FastAPI, Depends
from config import Config
from db import init_db
from routes import add_routers


def create_app(_config: Config):
    _app = FastAPI()

    @_app.get("/")
    def index():
        return {"message": "FastAPI starter template, Use freely"}

    add_routers(app=_app, config=_config)
    return _app


# Load configuration
config = Config.load_config()

# Create app
app = create_app(config)

# Initialize database
init_db(app)

if __name__ == '__main__':
    uvicorn.run("main:app", port=config.PORT, reload=True)
