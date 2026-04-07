import sqlalchemy as sa
from sqlalchemy import create_engine, String, Text, Boolean,Integer, DateTime, func, ForeignKey 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from app.models.base import Base
import uuid
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(50), nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True , nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    
    #bidirectional Relationship to MANY Tasks
    assigned_tasks: Mapped[list["Task"]] =relationship(back_populates="assigned_to")
    
    #bidirectional Relationship to MANY Projects
    assigned_projects: Mapped[list["Project"]] = relationship(back_populates="owner")
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "role": self.role,
            "is_admin": self.is_admin,
            "username": self.username,
            "email": self.email,
            #no password
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "assigned_projects": [project.to_dict() for project in self.assigned_projects] if self.assigned_projects else [],
            "assigned_tasks": [task.to_dict() for task in self.assigned_tasks] if self.assigned_tasks else [],
        }