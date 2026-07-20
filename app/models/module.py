from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    module_name = Column(String(100), unique=True, nullable=False)
    role_permissions = relationship("RolePermission", back_populates="module",cascade="all, delete")