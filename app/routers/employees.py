'''from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import EmployeeRegister
from app.crud.employee import create_employee

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/")
def create(data: EmployeeRegister, db: Session = Depends(get_db)):
    return create_employee(db, data)'''