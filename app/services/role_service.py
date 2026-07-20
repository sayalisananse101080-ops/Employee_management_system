from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.role_repository import RoleRepository
from app.schemas.role import RoleCreate, RoleUpdate


class RoleService:

    @staticmethod
    def create_role(db: Session, role: RoleCreate):

        existing_role = RoleRepository.get_role_by_name(
            db,
            role.role_name
        )

        if existing_role:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Role already exists."
            )

        return RoleRepository.create_role(db, role)

    @staticmethod
    def get_all_roles(db: Session):

        return RoleRepository.get_all_roles(db)

    @staticmethod
    def get_role_by_id(db: Session, role_id: int):

        role = RoleRepository.get_role_by_id(
            db,
            role_id
        )

        if role is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found."
            )

        return role

    @staticmethod
    def update_role(
        db: Session,
        role_id: int,
        role: RoleUpdate
    ):

        db_role = RoleRepository.get_role_by_id(
            db,
            role_id
        )

        if db_role is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found."
            )

        if (
            role.role_name is not None and
            role.role_name != db_role.role_name
        ):

            existing_role = RoleRepository.get_role_by_name(
                db,
                role.role_name
            )

            if existing_role:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Role name already exists."
                )

        return RoleRepository.update_role(
            db,
            db_role,
            role
        )

    @staticmethod
    def delete_role(
        db: Session,
        role_id: int
    ):

        db_role = RoleRepository.get_role_by_id(
            db,
            role_id
        )

        if db_role is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found."
            )

        RoleRepository.delete_role(
            db,
            db_role
        )

        return {
            "message": "Role deleted successfully."
        }