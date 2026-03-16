import sqlalchemy as sa
from sqlalchemy import create_engine, String, Text, Boolean,Integer, DateTime, func, ForeignKey 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from app.models.base import Base
import uuid
from datetime import datetime

    
class Sprint(Base):
    __tablename__ = "sprints"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    
    label: Mapped[str] = mapped_column(String, nullable = False)
    start_at: Mapped[datetime] = mapped_column(DateTime, nullable= False, server_default=func.now())
    end_at: Mapped[datetime] = mapped_column(DateTime, nullable= False)
    
    #create Sprint Relationship to MANY Task
    tasks: Mapped[list["Task"]] = relationship(back_populates="assigned_sprint")
    
