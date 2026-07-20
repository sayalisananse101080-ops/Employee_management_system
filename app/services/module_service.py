from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.module import Module
from app.repository.module_repository import ModuleRepository
from app.schemas.module import ModuleCreate, ModuleUpdate


class ModuleService:

    @staticmethod
    def create_module(db, module):
        return ModuleRepository.create_module(db, module)

    @staticmethod
    def get_all_modules(db: Session):

        return ModuleRepository.get_all_modules(db)

    @staticmethod
    def get_module_by_id(db: Session, module_id: int):

        module = ModuleRepository.get_module_by_id(
            db,
            module_id
        )

        if module is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Module not found."
            )

        return module

    @staticmethod
    def update_module(
        db: Session,
        module_id: int,
        module: ModuleUpdate
    ):

        db_module = ModuleRepository.get_module_by_id(
            db,
            module_id
        )

        if db_module is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Module not found."
            )

        return ModuleRepository.update_module(
            db,
            db_module,
            module
        )

    @staticmethod
    def delete_module(db: Session, module_id: int):

        db_module = ModuleRepository.get_module_by_id(
            db,
            module_id
        )

        if db_module is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Module not found."
            )

        ModuleRepository.delete_module(
            db,
            db_module
        )

        return {
            "message": "Module deleted successfully."
        }