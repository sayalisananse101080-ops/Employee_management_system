from enum import Enum
from datetime import datetime, date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field
class UserType(str, Enum):
    user="user"
    employee="employee"

# Base Schema
class UserBase(BaseModel):

    first_name: str = Field(
        ...,
        min_length=2,
        max_length=100
        #example="Sayali"
    )

    last_name: str = Field(
        ...,
        min_length=2,
        max_length=100
        #example="Sananse"
    )

    email: EmailStr = Field(
        ...
        #example="sayali@gmail.com"
    )

    phone: str = Field(
        ...,
        min_length=10,
        max_length=15,
        example="**********"
    )

    role_id: int = Field(
        ...,
        gt=0
        #example=1
    )

    status: bool = True
#create user
'''class UserCreate(UserBase):
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=100
        #example="Sayali"
    )

    last_name: str = Field(
        ...,
        min_length=2,
        max_length=100
        #example="Sananse"
    )

    email: EmailStr = Field(
        ...
        #example="sayali@gmail.com"
    )

    phone: str = Field(
        ...,
        min_length=10,
        max_length=15,
        example="99********"
    )
    password: str = Field(
        ...,
        min_length=6,
        max_length=255
    )
    role_id: int = Field(
        ...,
        gt=0
        #example=1
    )
    user_type: UserType
    department_id: int | None = None
    joining_date: date | None = None
    salary: float | None = None
'''
class UserCreate(UserBase):
    password: str = Field(..., min_length=6)
    user_type: UserType
    department_id: Optional[int] = None
    joining_date: Optional[date] = None
    salary: Optional[float] = None

#update user
class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None
    status: Optional[bool] = None
    user_type: Optional[UserType] = None
    department_id: Optional[int] = None
    joining_date: Optional[date] = None
    salary: Optional[float] = None


# Response Schema
class UserResponse(UserBase):
    id: int
    user_type: UserType
    department_id: Optional[int] = None
    joining_date: Optional[date] = None
    salary: Optional[float] = None
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class DepartmentResponse(BaseModel):
    id:int
    department_name:str
    description:str
    class Config:
        from_attributes = True

class RoleResponse(BaseModel):
    id:int
    role_name:str
    description:str |None=None
    class Config:
        from_attributes = True

class RolePermissionResponse(BaseModel):
    module_id:int
    module_name:str
    can_create:bool
    can_read:bool
    can_update:bool
    can_delete:bool
    can_view:bool
    
class MeResponse(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    phone:str
    status:bool
    user_type:str
    created_at:datetime
    updated_at:datetime
    
    joining_date:date |None
    salary: float |None
    department:DepartmentResponse |None
    role:RoleResponse
    role_permission:list[RolePermissionResponse]

    class Config:
        from_attributes = True