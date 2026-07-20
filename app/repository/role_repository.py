from sqlalchemy.orm import Session

from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate


class RoleRepository:

    @staticmethod
    def create_role(db: Session, role: RoleCreate):

        new_role = Role(
            role_name=role.role_name,
            description=role.description,
            status=role.status
        )

        db.add(new_role)
        db.commit()
        db.refresh(new_role)

        return new_role

    @staticmethod
    def get_all_roles(db: Session):

        return db.query(Role).all()

    @staticmethod
    def get_role_by_id(db: Session, role_id: int):

        return (
            db.query(Role)
            .filter(Role.id == role_id)
            .first()
        )

    @staticmethod
    def get_role_by_name(db: Session, role_name: str):

        return (
            db.query(Role)
            .filter(Role.role_name == role_name)
            .first()
        )

    @staticmethod
    def update_role(
        db: Session,
        db_role: Role,
        role: RoleUpdate
    ):

        update_data = role.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_role, key, value)

        db.commit()
        db.refresh(db_role)

        return db_role

    @staticmethod
    def delete_role(
        db: Session,
        db_role: Role
    ):

        db.delete(db_role)
        db.commit()

        return True