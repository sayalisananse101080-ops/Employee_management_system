from pydantic import BaseModel, Field, ConfigDict
from typing import List

# Base Schema
class RolePermissionBase(BaseModel):

    role_id: int
    module_id: int
    can_create: bool = False
    can_read: bool = False
    can_update: bool = False
    can_delete:bool = False
    can_view: bool = False

# Create Schema
class RolePermissionCreate(RolePermissionBase):
    pass

class RolePermissionUpdate(RolePermissionBase):
    pass

# Response Schema
class RolePermissionResponse(BaseModel):

    id: int
    role_id:int
    module_id:int
    can_create:bool
    can_read:bool
    can_update:bool
    can_delete:bool
    can_view:bool
    model_config =  ConfigDict(from_attributes=True)
    
