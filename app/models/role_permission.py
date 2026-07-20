from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False
    )

    module_id = Column(
        Integer,
        ForeignKey("modules.id", ondelete="CASCADE"),
        nullable=False
    )
    can_create = Column(Boolean, default=False)
    can_read = Column(Boolean, default=False)
    can_update = Column(Boolean, default=False)
    can_delete = Column(Boolean, default=False)
    can_view = Column(Boolean, default=False)

    role = relationship("Role", back_populates="role_permissions")
    module = relationship("Module",back_populates="role_permissions")