from sqlalchemy import Column, Integer, String, Boolean, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Department(Base):
    __tablename__="departments"

    id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(100),unique=True,nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP,server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(),onupdate=func.now())
    #designations = relationship("Designation",back_populates="department",cascade="all, delete-orphan")

    users= relationship("User",back_populates="department")
    employees = relationship(
    "Employee",
    back_populates="department"
)