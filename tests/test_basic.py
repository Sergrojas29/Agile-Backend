import unittest
import app.database
from init_db import setup_database, teardown_database


from app.database import SessionLocal
from app.models.user import User


class TestAppBasic(unittest.TestCase):
    
    
    def setUp(self) -> None:
        setup_database()

    def tearDown(self) -> None:
        teardown_database()
        
    def test_user(self)->None:
        with SessionLocal() as session:
            new_user = User(
                name= , 
        
            )