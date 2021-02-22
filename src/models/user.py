from passlib.context import CryptContext
from src.models.base.basemodel import ModelWithStatus, fields

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(ModelWithStatus):
    email = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=250)
    is_admin = fields.BooleanField(default=False)
    role = fields.ForeignKeyField('models.Role', related_name='users', null=True)

    @classmethod
    async def find_by_email(cls, email):
        return await cls.filter(email=email).first()

    @staticmethod
    def generate_hash(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_hash(password: str, hashed_password: str):
        return pwd_context.verify(password, hashed_password)

    class Meta:
        table = "users"

    class PydanticMeta:
        exclude = ['password']





