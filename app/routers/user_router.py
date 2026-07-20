from typing import List, Annotated, Union

from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)
from app.services.user_service import UserService
from app.security.jwt_bearer import get_current_user
from app.dependencies.permissions import permission_required
from app.schemas.user import MeResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
    #current_user = Depends(permission_required("Users","create"))
):
    return UserService.create_new_user(db, user)

@router.get("/",response_model=List[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user = Depends(permission_required("Users", "read"))
):
    return UserService.get_all_users(db)


@router.get("/me", response_model=MeResponse)
def get_me(
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return UserService.get_me(db,current_user)


@router.get("/{user_id}",response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    return UserService.get_user_by_id(db,user_id)


@router.put("/{user_id}",response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(permission_required("Users","update"))
):
    return UserService.update_user(db,user_id,user)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(permission_required("Users","delete"))
):
    return UserService.delete_user(db,user_id)
