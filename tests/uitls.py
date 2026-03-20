from dataclasses import dataclass
from init_db import setup_database, teardown_database

from app.models.user import User
from app.models.project import Project
from app.models.sprint import Sprint
from app.models.task import Task


from app.database import SessionLocal
from app.models.user import User



#Class Methods to create a testable Project Framework
#Allow API Front end testing
#
class FilloutDataBase:
    
    @classmethod
    def createTestDataBase(cls):
        #Create MANY Users
        
        #Creat ONE PROJECT
        
        #Creat ONE SPRINT
        
        #Create MANY TASKS
        
        #COMMIT TO DB
        pass 
        