from typing import Optional
from pydantic import Field
from .baseschema import BaseSchema


class RoleSchema(BaseSchema):
    role: str = Field(..., min_length=2, max_length=15)
    permissions: Optional[str]
