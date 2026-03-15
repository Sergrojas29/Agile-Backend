import sqlalchemy as sa
from sqlalchemy import create_engine, String, Text, Boolean,Integer, DateTime, func, ForeignKey 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from app.base import Base
from datetime import datetime
import uuid

# Class Import
from user import User
from sprint import Sprint

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable= True)
    
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    
    start_at: Mapped[datetime] = mapped_column(DateTime, nullable= False, server_default=func.now())
    due_at: Mapped[datetime] = mapped_column(DateTime, nullable= False)
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    
    #create Relationship to ONE user
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    assigned_to: Mapped["User"] = relationship(back_populates="assigned_tasks")
    
    #create Sprint Relationship to ONE sprint
    sprint_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sprints.id"))
    assigned_sprint: Mapped["Sprint"] = relationship(back_populates="tasks")