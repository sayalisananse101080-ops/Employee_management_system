from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.security.jwt_bearer import get_current_user
from app.repository.role_permission_repository import RolePermissionRepository
from app.models.role_permission import RolePermission
from app.models.module import Module

def permission_required(module_name: str, action: str):

    def checker(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
    ):
        '''print("Logged in user:", current_user.id)
        print("Role:", current_user.role_id)
        print("Module:", module_name)
        print("Action:", action)'''

        module = (
            db.query(Module)
            .filter(Module.module_name == module_name)
            .first()
        )

        if not module:
            raise HTTPException(
                status_code=404,
                detail="Module not found."
            )
        #print("Module Found:", module)

        permission = (
            db.query(RolePermission)
            .filter(
                RolePermission.role_id == current_user.role_id,
                RolePermission.module_id == module.id
            )
            .first()
        )

        if not permission:
            raise HTTPException(
                status_code=403,
                detail="Permission not found."
            )

        allowed = False

        if action == "create" and not permission.can_create:
            raise HTTPException(status_code=403, detail="Create permission denied")

        if action == "read" and not permission.can_read:
            raise HTTPException(status_code=403, detail="Read permission denied")

        if action == "update" and not permission.can_update:
            raise HTTPException(status_code=403, detail="Update permission denied")

        if action == "delete" and not permission.can_delete:
            raise HTTPException(status_code=403, detail="Delete permission denied")

        if action == "view" and not permission.can_view:
            raise HTTPException(status_code=403, detail="View permission denied")

        return current_user

    return checker