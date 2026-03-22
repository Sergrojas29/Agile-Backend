import unittest
from dataclasses import dataclass
from init_db import setup_database, teardown_database
from sqlalchemy.exc import IntegrityError
from datetime import date

from app.database import SessionLocal
from app.models.task import Task
from app.models.user import User
from app.models.sprint import Sprint
  
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
    
    # Test ONE - Sprint input
    def test_sprint(self)->None:
        one_sprint = Sprint(
            label = "Test sprint",
            start_at = date(2016, 3, 18),
            end_at = date(2016, 3, 18)
        )
            
        with SessionLocal() as session:
            session.add(one_sprint)
            
            #add test and check
            session.commit()
    
    
    
    # #Many Users
    def test_many_sprint(self)-> None:
        many_sprints: list[Sprint] = [ 
                   Sprint( label= "test 1" , start_at= date(2026, 3, 10), end_at= date(2026, 3, 24)),
                   Sprint( label= "test 2" , start_at= date(2026, 3, 25), end_at= date(2026, 4, 9)),
                   Sprint( label= "test 3" , start_at= date(2026, 4, 10), end_at= date(2026, 4, 19)),
                   Sprint( label= "test 4" , start_at= date(2026, 4, 20), end_at= date(2026, 5, 19)),
                   Sprint( label= "test 5" , start_at= date(2026, 5, 20), end_at= date(2026, 5, 29)),
                ]
 
        with SessionLocal() as session:
            
            session.add_all(many_sprints)
            session.commit()
            
            db_manu_users: list[User] = session.query(User).all()
            
            
            #User id isn't None
            for user in db_manu_users:
                self.assertIsNotNone(user.id)
            
            #Correct amount of user added
            self.assertEqual(len(db_manu_users), len(many_sprints))
            
            #Correct amount of Admins
            db_all_admin: list[User] = session.query(User).filter(User.is_admin == True).all()
            
            many_users_admins = [ user  for user in many_sprints if user.is_admin == True]
            
            self.assertEqual(len(db_all_admin), len(many_users_admins))
                
                