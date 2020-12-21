import uvicorn
from fastapi import FastAPI
from src.config.settings import Settings
from src.config.db import init_db
from src.routes import add_routers


def create_app(_config: Settings):
    _app = FastAPI()

    @_app.get("/")
    def index():
        return {"message": "FastAPI starter template, Use freely"}

    add_routers(app=_app, config=_config)
    return _app


# Load configuration
config = Settings.load_config()

# Create app
app = create_app(config)

# Initialize database
init_db(app)

if __name__ == '__main__':
    uvicorn.run("main:app", port=config.PORT, reload=True)
