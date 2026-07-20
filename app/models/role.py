from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)

    role_name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    description = Column(
        String(255),
        nullable=True
    )

    status = Column(
        Boolean,
        default=True
    )

    role_permissions = relationship(
    "RolePermission",
    back_populates="role",
    cascade="all, delete"
)
    
    users = relationship(
    "User",
    back_populates="role"
)