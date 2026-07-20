from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# ===============================
# Base Schema
# ===============================
class RoleBase(BaseModel):

    role_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        example="Admin"
    )

    description: Optional[str] = Field(
        default=None,
        max_length=255,
        example="System Administrator"
    )

    status: bool = Field(
        default=True,
        example=True
    )


# ===============================
# Create Schema
# ===============================
class RoleCreate(RoleBase):
    pass


# ===============================
# Update Schema
# ===============================
class RoleUpdate(BaseModel):

    role_name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100,
        example="HR"
    )

    description: Optional[str] = Field(
        default=None,
        max_length=255,
        example="Human Resource"
    )

    status: Optional[bool] = None


# ===============================
# Response Schema
# ===============================
class RoleResponse(BaseModel):

    id: int
    role_name:str
    description:str |None = None

    class Config:
        from_attributes = True