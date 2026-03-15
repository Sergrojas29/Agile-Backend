from sqlalchemy import create_engine, String
from sqlalchemy.orm import Mapped, mapped_column, Session , relationship, Boolean
from app.base import Base
from datetime import datetime
import uuid

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(50))
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True , nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=datetime.now())
    
    #bidirectional Relationship to MANY Tasks
    assigned_tasks: Mapped[list["Task"]] =relationship(back_populates="assigned_to")
    
    #bidirectional Relationship to MANY Projects
    assigned_projects: Mapped[list["Project"]] = relationship(back_populates="owner")