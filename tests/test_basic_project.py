import unittest
from dataclasses import dataclass
from init_db import setup_database, teardown_database
from sqlalchemy.exc import IntegrityError
from datetime import date

from app.database import SessionLocal
from app.models.task import Task
from app.models.user import User
from app.models.project import Project
  
#!  python -m unittest discover
class TestAppBasic(unittest.TestCase):
    
    
    def setUp(self) -> None:
        setup_database()
        one_user: User = User(name="Sergio", is_admin = True, username="SergProjectUsername", email="agood@gmail.com", password="Something")
                
 
        with SessionLocal() as session:
            
            session.add(one_user)
            session.flush()
            
            self.db_user_id = one_user.id
            session.commit()

    def tearDown(self) -> None:
        teardown_database()
    
    # Test One Project
    def test_one_project(self)->None:
        with SessionLocal() as session:
          
                        
            one_Project = Project(
                title = "One working Project",
                description = "This is a test project",
                start_at = date(2026, 3 , 20), #defualt to now()
                end_at = date(2026, 3 , 25),
                owner_id = self.db_user_id
            )
            
            session.add(one_Project)
            session.flush()
            
            session.expire(one_Project)
            db_project = session.query(Project).filter_by(title = one_Project.title).first()
            
            
            #Assert that is not NULL
            self.assertIsNotNone(db_project)
            # Assert Elements
            self.assertIsNotNone(db_project)
            self.assertEqual(db_project.title, "One working Project")
            self.assertEqual(db_project.description, "This is a test project")
            self.assertEqual(db_project.start_at, date(2026, 3, 20))
            self.assertEqual(db_project.end_at, date(2026, 3, 25))
            self.assertEqual(db_project.owner_id, self.db_user_id)
            
            session.commit()


    #Many projects
    def test_many_projects(self)-> None:
        with SessionLocal() as session:
            
            many_projects: list[Project] = [ 
                        Project(title = "One working Project",description = "This is a test project1",start_at = date(2026, 3 , 20), end_at = date(2026, 3 , 25),owner_id = self.db_user_id),
                        Project(title = "Two working Project",description = "This is a test project2",start_at = date(2026, 3 , 20), end_at = date(2026, 3 , 25),owner_id = self.db_user_id),
                        Project(title = "Three working Project",description = "This is a test project3",start_at = date(2026, 3 , 20), end_at = date(2026, 3 , 25),owner_id = self.db_user_id),
                    ]
            
            #ADD to Database
            session.add_all(many_projects)
            session.flush()
            
            #GET from database
            session.expire_all()
            db_many_porjects: list[Project] = session.query(Project).all()
            

            #ASSERT is not none
            self.assertIsNotNone(db_many_porjects)
            
            #Correct amount of Projects added
            self.assertEqual(len(db_many_porjects), 3)
            

    #Test Bad Project
    def test_invalid_project(self)-> None:
        with SessionLocal() as session:
            
            #NO OWNER ID - Invalid
            one_Project = Project(
                title = "One working Project",
                description = "This is a test project",
                start_at = date(2026, 3 , 20), #defualt to now()
                end_at = date(2026, 3 , 25)
                #NO OWNER ID
            )
            
            session.add(one_Project)
            
            with self.assertRaises(IntegrityError):
                session.commit()
            
            