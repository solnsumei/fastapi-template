from fastapi import Depends
from src.api import auth, roles
from src.utils.security import get_current_user


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
        roles.router,
        prefix=f"{config.API_URL}/roles",
        tags=["Roles"],
        dependencies=[Depends(get_current_user)]
    )
