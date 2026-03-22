import unittest
from dataclasses import dataclass
from init_db import setup_database, teardown_database
from sqlalchemy.exc import IntegrityError
from datetime import date

from app.database import SessionLocal
from app.models.task import Task
from app.models.user import User
from app.models.project import Project
from app.models.sprint import Sprint
  
#!  python -m unittest discover
class TestAppBasic(unittest.TestCase):
    pass
    
    def setUp(self) -> None:
        setup_database()
 
        with SessionLocal() as session:
            
            one_user = User(
                name="Sergio",
                is_admin=True,
                username="SergioUsername",
                email="agood@gmail.com",
                password="Something"
            )
            session.add(one_user)
            session.flush()

            #project in memory
            one_project = Project(
                title="One Working Project",
                description="This is a test project",
                start_at=date(2026, 3, 20),
                end_at=date(2026, 3, 25),
                owner_id=one_user.id
            )
            session.add(one_project)
            session.flush()
            
            one_sprint = Sprint(
            title = "Test sprint",
            start_at = date(2016, 3, 18),
            end_at = date(2016, 3, 25),
            project_id= one_project.id
            )
            
            session.add(one_sprint)
            session.commit()
            
            
            # Save IDs for use in tests
            self.user_id = one_user.id
            self.project_id = one_project.id
            self.sprint_id = one_sprint.id

    def tearDown(self) -> None:
        teardown_database()
        
    
    
    
    # ONE Task    
    def test_one_task(self)->None:
        
        with SessionLocal() as session:
            one_task = Task(
                title = "One Task",
                description = "This is the description of ONE task",
                start_at= date(2016, 3, 25),
                due_at= date(2016, 4, 24),
                value= 2,
                user_id= self.user_id,
                sprint_id= self.sprint_id
            )
            session.add(one_task)
            
            session.commit()
            




    # #Many Users
    # def test_many_user(self)-> None:
        many_task: list[Task] = [ 
                    Task(title= "task 1", description= "A good task description", start_at= date(2026, 4, 29), due_at= date(2026,5,20), value= 2, user_id = self.user_id, sprint_id= self.sprint_id),
                    Task(title= "task 1", description= "A good task description", start_at= date(2026, 4, 29), due_at= date(2026,5,20), value= 2, user_id = self.user_id, sprint_id= self.sprint_id),
                    Task(title= "task 1", description= "A good task description", start_at= date(2026, 4, 29), due_at= date(2026,5,20), value= 2, user_id = self.user_id, sprint_id= self.sprint_id),
                    Task(title= "task 1", description= "A good task description", start_at= date(2026, 4, 29), due_at= date(2026,5,20), value= 2, user_id = self.user_id, sprint_id= self.sprint_id),
                    Task(title= "task 1", description= "A good task description", start_at= date(2026, 4, 29), due_at= date(2026,5,20), value= 2, user_id = self.user_id, sprint_id= self.sprint_id),
                ]
 
        with SessionLocal() as session:
            
            session.add_all(many_task)
            session.commit()
            
            

                
                