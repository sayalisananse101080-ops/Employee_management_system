from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.department import(
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse
)
from app.dependencies.permissions import permission_required
from app.crud.department import(
    create_department,
    get_all_departments,
    get_department_by_id,
    update_department,
    delete_department,
    
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

#create api
@router.post("/", response_model=DepartmentResponse)
def create_new_department(
    department: DepartmentCreate,
    db:Session = Depends(get_db),
    current_user = Depends(
        permission_required("Department","create")
    )
):
    return create_department(db,department)


#get all
@router.get("/",response_model=list[DepartmentResponse])
def get_departments(
    db: Session = Depends(get_db),
    current_user = Depends(permission_required("Department", "read"))
):
    return get_all_departments(db)

#get by id
@router.get("/{department_id}", response_model= DepartmentResponse)
def get_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        permission_required("Department", "view")
    )
):
    department = get_department_by_id(db, department_id)

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )
    return department

#update
@router.put("/{department_id}", response_model=DepartmentResponse)
def update_existing_department(
    department_id: int,
    department: DepartmentUpdate,
    db:Session = Depends(get_db),
    current_user=Depends(
        permission_required("Department", "update")
    )
):
    updated = update_department(db, department_id, department)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )
    return updated

#delete
@router.delete("/{department_id}")
def remove_department(
    department_id: int,
    db:Session = Depends(get_db),
    current_user=Depends(
        permission_required("Department","delete")
    )
):
    deleted = delete_department(db, department_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return {
        "message": "Department deleted successfully."
    }