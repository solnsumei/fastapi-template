from typing import Optional, Any
from pydantic import BaseModel, validator, Field
from src.utils.status import Status


class BaseSchema(BaseModel):
    @validator('*', pre=True)
    def blank_strings(cls, v: Any):
        if type(v) == str:
            striped = v.strip()
            if striped == "":
                return None
            return striped

        return v


class StatusSchema(BaseSchema):
    status: Optional[Status] = Field(Status.ACTIVE)


class NameSchema(StatusSchema):
    name: str = Field(..., min_length=3, max_length=70, description="Name is required")


class NameDescriptionSchema(NameSchema):
    description: str
