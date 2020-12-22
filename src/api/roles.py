from .baserouter import BaseRouter
from src.models import Role, RolePydantic
from src.models.schema.role import RoleSchema


router = BaseRouter(
    model=Role,
    request_schema=RoleSchema,
    response_schema=RolePydantic
)

router.load_crud_routes()

