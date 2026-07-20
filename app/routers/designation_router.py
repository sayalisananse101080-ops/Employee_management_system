'''from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.designation import (
    DesignationCreate,
    DesignationUpdate,
    DesignationResponse,
)
from app.services.designation_services import DesignationService

router = APIRouter(
    prefix="/designations",
    tags=["Designation"],
)


@router.post("/", response_model=DesignationResponse)
def create_designation(
    designation: DesignationCreate,
    db: Session = Depends(get_db),
):
    return DesignationService.create_designation(
        db,
        designation,
    )


@router.get("/", response_model=list[DesignationResponse])
def get_designations(
    db: Session = Depends(get_db),
):
    return DesignationService.get_all_designations(db)


@router.get("/{designation_id}",
            response_model=DesignationResponse)
def get_designation(
    designation_id: int,
    db: Session = Depends(get_db),
):
    return DesignationService.get_designation(
        db,
        designation_id,
    )


@router.put("/{designation_id}",
            response_model=DesignationResponse)
def update_designation(
    designation_id: int,
    designation: DesignationUpdate,
    db: Session = Depends(get_db),
):
    return DesignationService.update_designation(
        db,
        designation_id,
        designation,
    )


@router.delete("/{designation_id}")
def delete_designation(
    designation_id: int,
    db: Session = Depends(get_db),
):
    return DesignationService.delete_designation(
        db,
        designation_id,
    )'''