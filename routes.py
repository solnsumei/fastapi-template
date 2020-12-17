from fastapi import Depends
from src.api import investments, properties, auth, pages
from src.utils import security


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

    app.include_router(
        investments.router,
        prefix=f"{config.API_URL}/investments",
        dependencies=[Depends(security.get_current_user)],
        tags=["Investments"]
    )

    app.include_router(
        pages.router,
        prefix=f"{config.API_URL}/pages",
        dependencies=[Depends(security.get_current_user)],
        tags=["Pages"]
    )

    app.include_router(
        properties.router,
        prefix=f"{config.API_URL}/properties",
        dependencies=[Depends(security.get_current_user)],
        tags=["Properties"]
    )
