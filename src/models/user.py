from passlib.context import CryptContext
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import fields
from .basemodel import BaseModel


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    email = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=250)
    is_admin = fields.BooleanField(default=False)

    @classmethod
    async def find_by_email(cls, email):
        return await cls.filter(email=email).first()

    @staticmethod
    def generate_hash(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_hash(password: str, hashed_password: str):
        return pwd_context.verify(password, hashed_password)

    class PydanticMeta:
        exclude = ('password',)


UserPydantic = pydantic_model_creator(User, name="User")
