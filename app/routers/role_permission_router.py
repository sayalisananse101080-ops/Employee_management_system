from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.module import ModuleResponse
from app.schemas.role_permission import (
    RolePermissionCreate,
    RolePermissionUpdate,
    RolePermissionResponse
)

from app.services.role_permission_service import (
    RolePermissionService
)
from app.security.jwt_bearer import get_current_user


router = APIRouter(
    prefix="/role-permissions",
    tags=["Role Permissions"]
)


@router.post(
    "/",
    response_model=RolePermissionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_role_permission(
    role_permission: RolePermissionCreate,
    db: Session = Depends(get_db)
):
    return RolePermissionService.create_role_permission(
        db,
        role_permission
    )


@router.get(
    "/",
    response_model=List[RolePermissionResponse]
)
def get_all_role_modules(
    db: Session = Depends(get_db)):
    return RolePermissionService.get_all_role_modules(db)

@router.put("/{mapping_id}")
def update_role_permission(
    mapping_id: int,
    role_permission: RolePermissionUpdate,
    db: Session = Depends(get_db)
):
    return RolePermissionService.update_role_permission(
        db,
        mapping_id,
        role_permission
    )

@router.get("/{mapping_id}")
def get_role_permission(
    mapping_id: int,
    db: Session = Depends(get_db)
):
    return RolePermissionService.get_role_permission(
        db,
        mapping_id
    )

@router.delete(
    "/{mapping_id}"
)

def delete_mapping(
    mapping_id: int,
    db: Session = Depends(get_db)
):
    return RolePermissionService.delete_mapping(
        db,
        mapping_id
    )


