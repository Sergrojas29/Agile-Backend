import unittest
from dataclasses import dataclass
from init_db import setup_database, teardown_database
from sqlalchemy.exc import IntegrityError
from datetime import date

from app.database import SessionLocal
from app.models.task import Task
from app.models.user import User
from app.models.sprint import Sprint
from app.models.project import Project
  
#!  python -m unittest discover
class TestAppBasic(unittest.TestCase):
    
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
            session.commit() 
            
            
            # Save IDs for use in tests
            self.user_id = one_user.id
            self.project_id = one_project.id
            

    def tearDown(self) -> None:
        teardown_database()
    
    # Test ONE - Sprint input
    def test_sprint(self)->None:
        one_sprint = Sprint(
            title = "Test sprint",
            start_at = date(2016, 3, 18),
            end_at = date(2016, 3, 25),
            project_id= self.project_id
        )
            
        with SessionLocal() as session:
            session.add(one_sprint)
            session.commit()
    
    
    
    # #Many sprint
    def test_many_sprint(self)-> None:
        many_sprints: list[Sprint] = [ 
                   Sprint( title= "test 1" , start_at= date(2026, 3, 10), end_at= date(2026, 3, 24),project_id= self.project_id),
                   Sprint( title= "test 2" , start_at= date(2026, 3, 25), end_at= date(2026, 4, 9),project_id= self.project_id),
                   Sprint( title= "test 3" , start_at= date(2026, 4, 10), end_at= date(2026, 4, 19), project_id= self.project_id),
                ]
 
        with SessionLocal() as session:
            
            session.add_all(many_sprints)
            session.commit()

            

                