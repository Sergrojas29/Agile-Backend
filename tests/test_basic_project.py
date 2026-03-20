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
        many_users: list[User] = [ 
                    User(name="Sergio", is_admin = True, username="SergioUsername", email="agood@gmail.com", password="Something"),
                    User(name="Carolina", is_admin=True, username="CarolinaUsername", email="aGood@gmail.com", password="passsssword"),
                    User(name="Mike", is_admin=False, username="MikeUsername", email="anotherGood1@gmail.com", password="pass11sssword"),
                    User(name="Andrew", is_admin=False, username="AndrewUsername", email="anotherGood45@gmail.com", password="pas$$$$sword"),
                    User(name="Eric", is_admin=True, username="EricUsername", email="AAanotherGood@gmail.com", password="p@aa$$sssword"),
                ]
 
        with SessionLocal() as session:
            
            session.add_all(many_users)
            session.commit()

    def tearDown(self) -> None:
        teardown_database()
    
    # Test One Project
    def test_one_task(self)->None:
        with SessionLocal() as session:
            
            #Created User for testing Owner
            db_user: User | None = session.query(User).filter_by(username= "SergioUsername").first()                
            
            
            one_Project = Project(
                name = "One working Project",
                description = "This is a invalid task",
                start_at = date(2026, 3 , 20), #defualt to now()
                end_at = date(2026, 3 , 25),
                owner_id = db_user.id
            )
            
            session.add(one_Project)
            
            db_project = session.query(Project).filter_by(name = one_Project.name).first()
            
            assert
            
            session.commit()
            
    
    
    
    
    # # ONE User    
    # def test_one_user(self)->None:
        
    #     with SessionLocal() as session:
    #         new_user = User(
    #             name= "Sergio Rojas", 
    #             role= "Is this need?",
    #             # isadmin -> default false
    #             username= "goodUsername", 
    #             email = "agood@gmail.com",#need email validation
    #             password= "Something"
    #         )
    #         session.add(new_user)
            
    #         session.commit()
            
            # user_db: User | None = session.query(User).filter_by(username= new_user.username).first()
            
    #         #Exists
    #         self.assertIsNotNone(user_db)
    #         self.assertIsNotNone(user_db.id)
            
    #         #Matchs input
    #         self.assertEqual(user_db.email, new_user.email)
    #         self.assertEqual(user_db.name, new_user.name)



    # #Many Users
    # def test_many_user(self)-> None:
    #     many_users: list[User] = [ 
    #                 User(name="Sergio Rojas", role="Is this need?", is_admin = True, username="goodUsername", email="agood@gmail.com", password="Something"),
    #                 User(name="Carolina ", is_admin=True, username="AnotherUsername", email="aGood@gmail.com", password="passsssword"),
    #                 User(name="Mike ", is_admin=False, username="ussssername", email="anotherGood1@gmail.com", password="pass11sssword"),
    #                 User(name="Andrew ", is_admin=False, username="stherUsername", email="anotherGood45@gmail.com", password="pas$$$$sword"),
    #                 User(name="Eric ", is_admin=True, username="usereNAme", email="AAanotherGood@gmail.com", password="p@aa$$sssword"),
    #             ]
 
    #     with SessionLocal() as session:
            
    #         session.add_all(many_users)
    #         session.commit()
            
    #         db_manu_users: list[User] = session.query(User).all()
            
            
    #         #User id isn't None
    #         for user in db_manu_users:
    #             self.assertIsNotNone(user.id)
            
    #         #Correct amount of user added
    #         self.assertEqual(len(db_manu_users), len(many_users))
            
    #         #Correct amount of Admins
    #         db_all_admin: list[User] = session.query(User).filter(User.is_admin == True).all()
            
    #         many_users_admins = [ user  for user in many_users if user.is_admin == True]
            
    #         self.assertEqual(len(db_all_admin), len(many_users_admins))
                
                