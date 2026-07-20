from sqlalchemy.orm import Session
from app.models.module import Module
from app.schemas.module import ModuleCreate, ModuleUpdate


class ModuleRepository:

    @staticmethod
    def create_module(db, module):
        print(module.__dict__)
        print(hasattr(module, "module_name"))

        new_module = Module(
            module_name=module.module_name
        )

        db.add(new_module)
        db.commit()
        db.refresh(new_module)

        return new_module

    @staticmethod
    def get_all_modules(db: Session):
        return db.query(Module).all()

    @staticmethod
    def get_module_by_id(db: Session, module_id: int):
        return (
            db.query(Module)
            .filter(Module.id == module_id)
            .first()
        )

    @staticmethod
    def update_module(
        db: Session,
        db_module: Module,
        module: ModuleUpdate
    ):

        update_data = module.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_module, key, value)

        db.commit()
        db.refresh(db_module)

        return db_module

    @staticmethod
    def delete_module(db: Session, db_module: Module):

        db.delete(db_module)
        db.commit()

        return True