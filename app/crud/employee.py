'''from sqlalchemy.orm import Session

from app.models.user import User
from app.models.employee import Employee

from app.utils.security import hash_password


def create_employee(db: Session, data):

    # ---------- STEP 5 ----------
    hashed_password = hash_password(data.password)

    new_user = User(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password=hashed_password,
        role_id=data.role_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # ---------- STEP 6 ----------
    employee = Employee(
        user_id=new_user.id,
        employee_code=data.employee_code,
        first_name=data.first_name,
        last_name=data.last_name,
        phone=data.phone,
        address=data.address,
        salary=data.salary,
        hire_date=data.hire_date
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee'''