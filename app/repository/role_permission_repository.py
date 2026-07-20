from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.role_permission import RolePermission
from app.schemas.role_permission import RolePermissionCreate


class RolePermissionRepository:

    @staticmethod
    def create_role_permission(db,role_permission):

        new_role_permission = RolePermission(
            role_id=role_permission.role_id,
            module_id=role_permission.module_id,
            can_create=role_permission.can_create,
            can_read=role_permission.can_read,
            can_update=role_permission.can_update,
            can_delete=role_permission.can_delete,
            can_view=role_permission.can_view
        )

        db.add(new_role_permission)
        db.commit()
        db.refresh(new_role_permission)

        return new_role_permission

    @staticmethod
    def get_all_role_modules(
        db
    ):

        return db.query(RolePermission).all()

    @staticmethod
    def get_by_id(
        db,
        mapping_id
    ):

        return (
            db.query(RolePermission)
            .filter(RolePermission.id == mapping_id)
            .first()
        )

    @staticmethod
    def get_module_by_role(
        db,
        role_id
    ):

        return (
            db.query(RolePermission)
            .filter(RolePermission.role_id == role_id)
            .all()
        )

    @staticmethod
    def get_by_module_id(
        db: Session,
        module_id: int
    ):

        return (
            db.query(RolePermission)
            .filter(RolePermission.module_id == module_id)
            .all()
        )

    @staticmethod
    def check_duplicate(
        db: Session,
        role_id: int,
        module_id: int
    ):

        return (
            db.query(RolePermission)
            .filter(
                RolePermission.role_id == role_id,
                RolePermission.module_id == module_id
            )
            .first()
        )
    
    @staticmethod
    def get_role_permission(db, mapping_id):

        permission = (
            db.query(RolePermission)
            .filter(RolePermission.id == mapping_id)
            .first()
        )

        if permission is None:
            raise HTTPException(
                status_code=404,
                detail="Role Permission not found"
            )

        return permission
    
    from fastapi import HTTPException

    @staticmethod
    def update_role_permission(db, mapping_id, role_permission):

        db_permission = (
            db.query(RolePermission)
            .filter(RolePermission.id == mapping_id)
            .first()
        )

        if db_permission is None:
            raise HTTPException(
                status_code=404,
                detail="Role Permission not found"
            )

        db_permission.role_id = role_permission.role_id
        db_permission.module_id = role_permission.module_id
        db_permission.can_create = role_permission.can_create
        db_permission.can_read = role_permission.can_read
        db_permission.can_update = role_permission.can_update
        db_permission.can_delete = role_permission.can_delete

        db.commit()
        db.refresh(db_permission)

        return db_permission

    @staticmethod
    def delete_mapping(
        db: Session,
        mapping: RolePermission
    ):

        db.delete(mapping)
        db.commit()

        return True
    
    @staticmethod
    def get_permission_for_role(
        db: Session,
        role_id: int,
        module_name: str
    ):
        from app.models.module import Module

        return (
            db.query(Module)
            .join(RolePermission, RolePermission.module_id == Module.id)
            .filter(
                RolePermission.role_id == role_id,
                Module.module == module_name
            )
            .first()
        )
  