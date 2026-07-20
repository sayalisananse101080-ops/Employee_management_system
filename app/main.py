from fastapi import FastAPI, Depends

# Import models so SQLAlchemy knows about them
from app.models.role import Role
from app.models.module import Module
from app.models.role_permission import RolePermission
from app.models.user import User
from app.models.department import Department
#from app.models.designation import Designation
from app.models.employee import Employee
from app.routers.module_router import router as module_router
from app.routers.role_router import router as role_router
from app.routers.role_permission_router import (router as role_permission_router)
from app.routers.user_router import router as user_router
from app.routers.auth_router import router as auth_router  
from app.routers import department_router
#from app.routers import designation_router
# Create all tables

app = FastAPI(
    title="Employee Management System",
    description="Role Based Access Control (RBAC) API",
    version="1.0.0"
)

# Register Routers
app.include_router(module_router)
app.include_router(role_router)
app.include_router(role_permission_router)
app.include_router(user_router)
app.include_router(auth_router)    
app.include_router(department_router.router)
#app.include_router(designation_router.router)
@app.get("/")
def home():
    return {
        "success": True,
        "message": "Employee Management System API is Running"
    }

from app.security.jwt_bearer import get_current_user

