import sqlalchemy as sa
from sqlalchemy import create_engine, String, Text, Boolean,Integer, DateTime, func, ForeignKey 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from app.database import Base
import uuid
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(50))
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True , nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    
    #bidirectional Relationship to MANY Tasks
    assigned_tasks: Mapped[list["Task"]] =relationship(back_populates="assigned_to")
    
    #bidirectional Relationship to MANY Projects
    assigned_projects: Mapped[list["Project"]] = relationship(back_populates="owner")