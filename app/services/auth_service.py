from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.auth import verify_password, create_access_token
from app.repository.user_repository import UserRepository


class AuthService:

    @staticmethod
    def login(db: Session, email: str, password: str):

        user = UserRepository.get_user_by_email(db, email)

        if user is None or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        if not user.status:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive."
            )

        token_data = {
            "sub": str(user.id),
            "role_id": user.role_id
        }

        access_token = create_access_token(token_data)

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }