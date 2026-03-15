import unittest
from init_db import setup_database, teardown_database


from app.database import SessionLocal
from app.models.user import User

#!  python -m unittest discover
class TestAppBasic(unittest.TestCase):
    
    
    def setUp(self) -> None:
        setup_database()

    def tearDown(self) -> None:
        teardown_database()
        
    def test_user(self)->None:
        with SessionLocal() as session:
            new_user = User(
                name= "Sergio Rojas", 
                role= "Is this need?",
                # isadmin -> default false
                username= "serg", #need email validation
                email = "serg@gmail.com",
                password= "Something"
            )
            session.add(new_user)
            
            session.commit()
            
            fetch_user = session.query(User).all()
            for user in fetch_user:
                print(user.name)
                print(user.email)
                print(user.role)