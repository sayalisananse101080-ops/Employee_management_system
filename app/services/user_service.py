from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from passlib.context import CryptContext

from app.schemas.user import UserCreate, UserUpdate
from app.auth import hash_password
from app.models.user import User
from app.crud import user as user_crud
from app.repository.user_repository import UserRepository
from app.models.role_permission import RolePermission
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class UserService:

    @staticmethod
    def create_new_user(
        db: Session,
        user: UserCreate
    ):

        # Check Email Exists
        existing_email = user_crud.get_by_email(db, user.email)

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )
        
        # Check phone already exists
        existing_phone = db.query(User).filter(
            User.phone == user.phone
        ).first()

        if existing_phone:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone already exists"
            )
        
         #Employee/User Validation
        if user.user_type == "employee":
            if (
                user.department_id is None
                or user.joining_date is None
                or user.salary is None
            ):
                raise HTTPException(
                    status_code=400,
                    detail="Department, Joining Date and Salary are required for Employee."
                )

        if user.user_type == "user":
            user.department_id = None
            user.joining_date = None
            user.salary = None

        # Create new user
        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            password=hash_password(user.password),   # IMPORTANT
            role_id=user.role_id,
            user_type= user.user_type,
            department_id=user.department_id,
            joining_date=user.joining_date,
            salary=user.salary,
            status=user.status
        )

        return user_crud.create(db, new_user)
    

    @staticmethod
    def get_all_users(
        db: Session
    ):
        return user_crud.get_all(db)
    
    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: int
    ):

        user = db.query(User).filter(
            User.id == user_id
        ).first()
        

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )

        return user

    @staticmethod
    def update_user(
        db: Session,
        user_id: int,
        user: UserUpdate
    ):

        db_user = user_crud.get_by_id(db, user_id)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if user.first_name is not None:
            db_user.first_name = user.first_name

        if user.last_name is not None:
            db_user.last_name = user.last_name

        if user.email is not None:
            db_user.email = user.email

        if user.phone is not None:
            db_user.phone = user.phone

        if user.password is not None:
            db_user.password = hash_password(user.password)

        if user.role_id is not None:
            db_user.role_id = user.role_id

        if user.status is not None:
            db_user.status = user.status

        #employee/user
        if user.user_type is not None:
            db_user.user_type = user.user_type
        if db_user.user_type == "employee":

            if user.department_id is not None:
                db_user.department_id = user.department_id

            if user.joining_date is not None:
                db_user.joining_date = user.joining_date

            if user.salary is not None:
                db_user.salary = user.salary

        else:
            db_user.department_id = None
            db_user.joining_date = None
            db_user.salary = None
        

        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def delete_user(
        db: Session,
        user_id: int
    ):

        user = db.query(User).filter(
            User.id == user_id
        ).first()


        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )
        
        db.delete(user)
        db.commit()

        return {
            "message": "User deleted successfully."
        }
    
    @staticmethod
    def get_me(db, current_user):
        user= UserRepository.get_me(db, current_user.id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not Found"
            )
        
        modules = (db.query(RolePermission).filter(RolePermission.role_id ==user.role_id).all())
        modules_list = []

        for permission in modules:
            modules_list.append(
                {
                    "module_id":permission.module.id,
                    "module_name": permission.module.module_name,
                    "can_create": permission.can_create,
                    "can_read": permission.can_read,
                    "can_update": permission.can_update,
                    "can_delete": permission.can_delete,
                    "can_view": permission.can_view
                }
            )

        return{
            "id":user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "status": user.status,
            "user_type": user.user_type,
            "created_at": user.created_at,
            "updated_at":user.updated_at,

            "joining_date": user.joining_date if user.user_type== "employee" else None,
            "salary": user.salary if user.user_type=="employee" else None,

            "department":{
                "id": user.department.id,
                "department_name": user.department.department_name,
                "description": user.department.description
            } if user.user_type == "employee" and user.department else None,

            "role":{
                "id":user.role.id,
                "role_name":user.role.role_name,
                "description": user.role.description
            },
            "role_permission":modules_list
        }
            
