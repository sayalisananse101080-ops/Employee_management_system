from sqlalchemy import Column, Integer, String, Numeric, Date, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    employee_code = Column(String(50), unique=True, nullable=False)
    first_name=Column(String(100))
    last_name=Column(String(100))
    phone=Column(String(15))
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    #designation = Column(String(100), nullable=False)
    salary = Column(Numeric(10, 2), nullable=False)
    joining_date = Column(Date, nullable=False)
    address = Column(String(255), nullable=True)
    hire_date=Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="employee")
    department = relationship("Department",back_populates="employees")