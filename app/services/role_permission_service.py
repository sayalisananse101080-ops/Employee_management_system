from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repository.role_permission_repository import RolePermissionRepository
from app.repository.role_repository import RoleRepository
from app.repository.module_repository import ModuleRepository

from app.schemas.role_permission import RolePermissionCreate


class RolePermissionService:

    @staticmethod
    def create_role_permission(
        db: Session,
        role_permission: RolePermissionCreate
    ):

        # Check Role Exists
        role = RoleRepository.get_role_by_id(
            db,
            role_permission.role_id
        )

        if role is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Role not found."
            )

        # Check module Exists
        module = ModuleRepository.get_module_by_id(
            db,
            role_permission.module_id
        )

        if module is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Modules not found."
            )

        # Check Duplicate Mapping
        mapping = RolePermissionRepository.check_duplicate(
            db,
            role_permission.role_id,
            role_permission.module_id
        )

        if mapping:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Module already assigned to this role."
            )

        return RolePermissionRepository.create_role_permission(
            db,
            role_permission
        )
    
    @staticmethod
    def update_role_permission(db, mapping_id, role_permission):
        return RolePermissionRepository.update_role_permission(
            db,
            mapping_id,
            role_permission
        )

    @staticmethod
    def get_all_role_modules(db):
        return RolePermissionRepository.get_all_role_modules(db)

    @staticmethod
    def get_role_permission(db, mapping_id):
        return RolePermissionRepository.get_role_permission(
            db,
            mapping_id
        )

    @staticmethod
    def delete_mapping(
        db: Session,
        mapping_id: int
    ):

        mapping = RolePermissionRepository.get_by_id(
            db,
            mapping_id
        )

        if mapping is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mapping not found."
            )

        RolePermissionRepository.delete_mapping(
            db,
            mapping
        )

        return {
            "message": "Role Permission deleted successfully."
        }
    