from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from .role import Role
from .user import User


# Initialize model relationships
Tortoise.init_models(["src.models"], "models")

# User serialization
UserPydantic = pydantic_model_creator(User, exclude=("role",))
UserWithRelations = pydantic_model_creator(User, name="UserWithRelations")

# Role serialization
RolePydantic = pydantic_model_creator(Role, exclude=("users",))
RoleWithRelations = pydantic_model_creator(Role, name="RoleWithRelations")
