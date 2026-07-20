'''from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.database import Base

class Designation(Base):
    __tablename__= "designations"

    id = Column(Integer, primary_key=True, index=True)
    designation_name = Column(String(100), unique=True, nullable= False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    description = Column(String(255),nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text(
        "CURRENT_TIEMSTAMP ON UPDATE CURRENT_TIMESTAMP"
    ))
    department = relationship("Department",back_populates="designations")'''