from src.api import auth


def add_routers(app, config):
    """
    Include routes
    :param app:
    :param config:
    :return: None
    """
    app.include_router(
        auth.router,
        prefix=f"{config.API_URL}/auth",
        tags=["Authentication"]
    )
