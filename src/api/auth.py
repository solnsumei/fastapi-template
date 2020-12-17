from .baserouter import APIRouter
from src.models.schema.user import AuthSchema
from src.utils.security import create_token, authenticate
from src.models import UserPydantic


router = APIRouter()


@router.post('/login')
async def login_user(auth: AuthSchema):
    user = await authenticate(auth.email, auth.password)
    token = create_token({"sub": user.email})
    user_pydantic = await UserPydantic.from_tortoise_orm(user)

    return {
        "user": user_pydantic,
        "token": token
    }
