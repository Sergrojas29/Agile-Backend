import sqlalchemy as sa
from sqlalchemy import create_engine, String, Text, Boolean,Integer, DateTime, func, ForeignKey , Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from app.models.base import Base
from datetime import datetime
import uuid


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable= True)
    
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    
    start_at: Mapped[Date] = mapped_column(Date, nullable= False, server_default=func.now())
    due_at: Mapped[Date] = mapped_column(Date, nullable= False)
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    complete: Mapped[bool] = mapped_column(Boolean, default=False)
    
    #create Relationship to ONE user
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    assigned_to: Mapped["User"] = relationship(back_populates="assigned_tasks")
    
    #create Sprint Relationship to ONE sprint
    sprint_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sprints.id"))
    assigned_sprint: Mapped["Sprint"] = relationship(back_populates="tasks")
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "start_at": self.start_at if self.start_at else None,
            "due_at": self.due_at if self.due_at else None,
            "value": self.value,
            "complete": self.complete,
            
            "user_id": str(self.user_id) if self.user_id else None,
            "sprint_id": str(self.sprint_id) if self.sprint_id else None
        }