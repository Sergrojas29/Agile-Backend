import sqlalchemy as sa
from sqlalchemy import create_engine, String, Text, Boolean,Integer, DateTime, func, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from app.models.base import Base
import uuid
from datetime import datetime



class Project(Base):
    __tablename__ = "projects"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    
    description: Mapped[str] = mapped_column(String(500), nullable= True)
    
    start_at: Mapped[Date] = mapped_column(Date, nullable= False, server_default=func.now())
    end_at: Mapped[Date] = mapped_column(Date, nullable= False)
    
    
    #!TODO: assign project to many users
    #create Relationship to MANY users
    # team: Mapped[list["User"]] = mapped_column()
    
    #create Relationship to ONE user
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="assigned_projects")
    
    
    #create Relationshio to MANY Sprints
    assigned_sprints: Mapped[list["Sprint"]] = relationship(back_populates="project",
                                                            cascade="all, delete-orphan"
                                                            )
    
