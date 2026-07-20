from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:

    @staticmethod
    def create_new_user(db: Session, user: UserCreate):

        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            password=user.password,
            role_id=user.role_id,
            status=user.status
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def get_all_users(db: Session):

        return db.query(User).all()

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def get_user_by_email(db: Session, email: str):

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def update_user(
        db: Session,
        user: User,
        user_data: UserUpdate
    ):

        update_data = user_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def delete_user(db: Session, user: User):

        db.delete(user)
        db.commit()

        return True
    
    @staticmethod
    def get_me(db:Session,user_id:int):
        return(db.query(User).filter(User.id == user_id).first())
    