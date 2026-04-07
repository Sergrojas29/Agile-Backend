import sqlalchemy as sa
from sqlalchemy import create_engine, String, Text, Boolean,Integer, DateTime, func, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from app.models.base import Base
import uuid
from datetime import datetime

    
class Sprint(Base):
    __tablename__ = "sprints"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    
    title: Mapped[str] = mapped_column(String, nullable = False)
    start_at: Mapped[Date] = mapped_column(Date, nullable= False, server_default=func.now())
    end_at: Mapped[Date] = mapped_column(Date, nullable= False)
    
    #create Relationship to ONE project
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"))
    project: Mapped["Project"] = relationship(back_populates="assigned_sprints")
    
    #create Sprint Relationship to MANY Task
    tasks: Mapped[list["Task"]] = relationship(back_populates="assigned_sprint",
                                                            cascade="all, delete-orphan"
                                                            )
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "start_at": self.start_at if self.start_at else None,
            "end_at": self.end_at if self.end_at else None,
            "project_id": str(self.project_id),
            "tasks": [task.to_dict() for task in self.tasks] if self.tasks else []
            
        }
