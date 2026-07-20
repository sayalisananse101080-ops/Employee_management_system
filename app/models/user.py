import enum
from sqlalchemy import (Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric, Date, Enum,DECIMAL)
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

'''class UserType(str, enum.Enum):
    user = "user"
    employee = "employee"
'''
class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=False)
    email = Column(String(255),unique=True,nullable=False)
    phone = Column(String(20),unique=True,nullable=False)
    password = Column(String(255),nullable=False)
    role_id = Column(Integer,ForeignKey("roles.id"),nullable=False)
    employee_code= Column(String,nullable= True,unique=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    salary = Column(DECIMAL(10,2), nullable=True)
    joining_date = Column(Date, nullable=True)
    address = Column(String(200),nullable=False)
    status = Column(Boolean,default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_type = Column(Enum("user","employee"),nullable=False)
    department = relationship("Department", back_populates="users")
    role = relationship("Role",back_populates="users")
    employee = relationship(
    "Employee",
    back_populates="user",
    uselist=False
)