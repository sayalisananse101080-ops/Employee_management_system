from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.role import (
    RoleCreate,
    RoleUpdate,
    RoleResponse
)
from app.services.role_service import RoleService
from app.dependencies.permissions import permission_required

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post(
    "/",
    response_model=RoleResponse,
    status_code=status.HTTP_201_CREATED
)
def create_role(
    role: RoleCreate,
    db: Session = Depends(get_db),
    current_user = Depends(
        permission_required("Role","create")
    )
):
    return RoleService.create_role(db, role)


@router.get(
    "/",
    response_model=List[RoleResponse]
)
def get_all_roles(
    db: Session = Depends(get_db),
    current_user=Depends(
        permission_required("Role", "read")
    )
):
    return RoleService.get_all_roles(db)


@router.get(
    "/{role_id}",
    response_model=RoleResponse
)
def get_role_by_id(
    role_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        permission_required("Role","view")
    )
):
    return RoleService.get_role_by_id(db, role_id)


@router.put(
    "/{role_id}",
    response_model=RoleResponse
)
def update_role(
    role_id: int,
    role: RoleUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        permission_required("Role","update")
    )
):
    return RoleService.update_role(
        db,
        role_id,
        role
    )


@router.delete(
    "/{role_id}"
)
def delete_role(
    role_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        permission_required("Role","delete")
    )
):
    return RoleService.delete_role(
        db,
        role_id
    )