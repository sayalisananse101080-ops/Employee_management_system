from sqlalchemy.orm import Session
from app.models.user import User
#from app.repository.user_repository import UserRepository
#from app.repository.role_repository import RoleRepository

def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone == phone).first()


def get_all(db: Session):
    return db.query(User).all()


def create(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session, user: User):
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: User):
    db.delete(user)
    db.commit()