from .basemodel import BaseModel, fields


class Role(BaseModel):
    role = fields.CharField(max_length=20, unique=True)
    permissions = fields.CharField(max_length=250, null=True)

    class Meta:
        table = "roles"

    class PydanticMeta:
        exclude = ("created_at",)
