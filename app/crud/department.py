from sqlalchemy.orm import Session
from app.models.department import Department

def create_department(db:Session, department:int):

    new_department = Department(**department.dict())
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

# Get All Departments
def get_all_departments(db: Session):
    return db.query(Department).all()


#get ID
def get_department_by_id(db:Session,department_id:int):
    return db.query(Department
    ).filter(
        Department.id == department_id
    ).first()

#update Department
def update_department(db:Session,department_id:int,department):
    db_department = get_department_by_id(db,department_id)

    if not db_department:
        return None

    for key, value in department.dict(exclude_unset=True).items():
        setattr(db_department, key, value)

    db.commit()
    db.refresh(db_department)
    return db_department

#delete Department
def delete_department(db:Session,department_id:int):
    db_department = get_department_by_id(db, department_id)
    if not db_department:
        return None
    
    db.delete(db_department)
    db.commit()
    return db_department
