from pydantic import EmailStr
from .baseschema import BaseSchema


class AuthSchema(BaseSchema):
    email: EmailStr
    password: str

