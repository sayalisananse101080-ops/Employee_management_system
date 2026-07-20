from pydantic import BaseModel
from datetime import datetime
#base schema
class DepartmentBase(BaseModel):
    department_name: str
    description: str | None = None
    is_active: bool = True
#create schema
class DepartmentCreate(BaseModel):
    department_name: str
    description: str | None = None
    is_active: bool
#update schema
class DepartmentUpdate(BaseModel):
    department_name: str
    description: str | None = None
    is_active: bool
#response schema
class DepartmentResponse(BaseModel):
    id: int
    department_name:str
    description:str

    class Config:
        from_attributes = True