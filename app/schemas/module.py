from pydantic import BaseModel, ConfigDict
#from typing import Optional


class ModuleBase(BaseModel):
    module_name: str
    
class ModuleCreate(ModuleBase):
    pass

class ModuleUpdate(ModuleBase):
    pass

class ModuleResponse(ModuleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
class ModuleDelete (ModuleBase):
    pass