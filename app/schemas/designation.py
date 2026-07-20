'''from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class DesignationCreate(BaseModel):
    designation_name:str
    department_id:int
    description:Optional[str]=None

class DesignationUpdate(BaseModel):
    designation_name:Optional[str] = None
    department_id:Optional[int] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class DesignationResponse(BaseModel):
    id: int
    designation_name: str
    department_id: int
    description: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True'''