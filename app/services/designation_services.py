'''from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud import designation as designation_crud
from app.crud import department as department_crud
from app.models.designation import Designation
from app.schemas.designation import (
    DesignationCreate,
    DesignationUpdate,
)


class DesignationService:

    @staticmethod
    def create_designation(
        db: Session,
        designation: DesignationCreate,
    ):

        if designation_crud.get_by_name(
            db,
            designation.designation_name
        ):
            raise HTTPException(
                status_code=400,
                detail="Designation already exists"
            )

        department = department_crud.get_by_id(
            db,
            designation.department_id
        )

        if not department:
            raise HTTPException(
                status_code=404,
                detail="Department not found"
            )

        new_designation = Designation(**designation.model_dump())

        return designation_crud.create(
            db,
            new_designation
        )

    @staticmethod
    def get_all_designations(db: Session):
        return designation_crud.get_all(db)

    @staticmethod
    def get_designation(db: Session, designation_id: int):

        designation = designation_crud.get_by_id(
            db,
            designation_id
        )

        if not designation:
            raise HTTPException(
                status_code=404,
                detail="Designation not found"
            )

        return designation

    @staticmethod
    def update_designation(
        db: Session,
        designation_id: int,
        designation_data: DesignationUpdate,
    ):

        designation = designation_crud.get_by_id(
            db,
            designation_id
        )

        if not designation:
            raise HTTPException(
                status_code=404,
                detail="Designation not found"
            )

        update_data = designation_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(designation, key, value)

        return designation_crud.update(
            db,
            designation
        )

    @staticmethod
    def delete_designation(
        db: Session,
        designation_id: int,
    ):

        designation = designation_crud.get_by_id(
            db,
            designation_id
        )

        if not designation:
            raise HTTPException(
                status_code=404,
                detail="Designation not found"
            )

        designation_crud.delete(
            db,
            designation
        )

        return {
            "message": "Designation deleted successfully"
        }'''