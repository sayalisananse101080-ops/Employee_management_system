from fastapi import APIRouter, Depends, status, FastAPI
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.module import (
    ModuleCreate,
    ModuleUpdate,
    ModuleResponse
)
from app.services.module_service import ModuleService
from app.database import Base, engine
from app.models.module import Module
from app.schemas.module import(
    ModuleCreate, ModuleUpdate, ModuleResponse)

Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/module",
    tags=["Module"]
)


# ===========================
# Create Module
# ===========================
@router.post(
    "/",
    response_model=ModuleResponse,
    status_code=status.HTTP_201_CREATED
)
def create_module(
    module: ModuleCreate,
    db: Session = Depends(get_db)
):
    print(module)
    print(type(module))
    print(module.model_dump())
    return ModuleService.create_module(
        db,
        module
    )


# ===========================
# Get All Module
# ===========================
@router.get(
    "/",
    response_model=List[ModuleResponse]
)
def get_all_modules(
    db: Session = Depends(get_db)
):
    return ModuleService.get_all_modules(db)


# ===========================
# Get Module By ID
# ===========================
@router.get(
    "/{module_id}",
    response_model=ModuleResponse
)
def get_module(
    module_id: int,
    db: Session = Depends(get_db)
):
    return ModuleService.get_module_by_id(
        db,
        module_id
    )


# ===========================
# Update Module
# ===========================
@router.put(
    "/{module_id}",
    response_model=ModuleResponse
)
def update_permission(
    module_id: int,
    module: ModuleUpdate,
    db: Session = Depends(get_db)
):
    return ModuleService.update_module(
        db,
        module_id,
        module
    )


# ===========================
# Delete Module
# ===========================
@router.delete(
    "/{module_id}"
)
def delete_module(
    module_id: int,
    db: Session = Depends(get_db)
):
    return ModuleService.delete_module(
        db,
        module_id
    )