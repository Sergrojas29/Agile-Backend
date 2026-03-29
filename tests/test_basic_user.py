import unittest
from dataclasses import dataclass
from init_db import setup_database, teardown_database
from sqlalchemy.exc import IntegrityError



from app.database import SessionLocal
from app.models.user import User

  
#!  python -m unittest discover
class TestAppBasic(unittest.TestCase):
    
    
    def setUp(self) -> None:
        setup_database()

    def tearDown(self) -> None:
        teardown_database()
    
    # Test Bad user input
    def test_zero_user(self)->None:
        with SessionLocal() as session:
            
            bad_user = User(
                name= "Sergio Rojas", 
                # isadmin -> default false
                username= "goodUsername", 
                # missing email
                # email = "agood@gmail.com",#need email validation
                password= "Something"
            )
            
            session.add(bad_user)
            
            with self.assertRaises(IntegrityError):
                session.commit()
            
    
    # ONE User    
    def test_one_user(self)->None:
        
        with SessionLocal() as session:
            new_user = User(
                name= "Sergio Rojas", 
                # isadmin -> default false
                username= "goodUsername", 
                email = "agood@gmail.com",#need email validation
                password= "Something"
            )
            session.add(new_user)
            
            session.commit()
            
            user_db: User | None = session.query(User).filter_by(username= new_user.username).first()
            
            #Exists
            self.assertIsNotNone(user_db)
            self.assertIsNotNone(user_db.id)
            
            #Matchs input
            self.assertEqual(user_db.email, new_user.email)
            self.assertEqual(user_db.name, new_user.name)



    #Many Users
    def test_many_user(self)-> None:
        many_users: list[User] = [ 
                    User(name="Sergio", is_admin = True, username="goodUsername", email="agood@gmail.com", password="Something"),
                    User(name="Carolina", is_admin=True, username="CarolinaUsername", email="aGood@gmail.com", password="passsssword"),
                    User(name="Mike", is_admin=False, username="MikeUssername", email="anotherGood1@gmail.com", password="pass11sssword"),
                    User(name="Andrew", is_admin=False, username="stherUsername", email="anotherGood45@gmail.com", password="pas$$$$sword"),
                    User(name="Eric", is_admin=True, username="usereNAme", email="AAanotherGood@gmail.com", password="p@aa$$sssword"),
                ]
 
        with SessionLocal() as session:
            
            session.add_all(many_users)
            session.commit()
            
            db_manu_users: list[User] = session.query(User).all()
            
            
            #User id isn't None
            for user in db_manu_users:
                self.assertIsNotNone(user.id)
            
            #Correct amount of user added
            self.assertEqual(len(db_manu_users), len(many_users))
            
            #Correct amount of Admins
            db_all_admin: list[User] = session.query(User).filter(User.is_admin == True).all()
            
            many_users_admins = [ user  for user in many_users if user.is_admin == True]
            
            self.assertEqual(len(db_all_admin), len(many_users_admins))
                
                