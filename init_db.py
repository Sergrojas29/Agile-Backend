from app.database import engine
from app.models.base import Base
# put this on render
# pip install -r requirements.txt && python init_db.py

from app.models.user import User
from app.models.project import Project
from app.models.sprint import Sprint
from app.models.task import Task


"""
Teardown Database for Testing
"""
def teardown_database():

    
    Base.metadata.drop_all(bind=engine)


"""
Initializing Database for Deployment
# pip install -r requirements.txt && python init_db.py
"""
def setup_database():
    print("Initializing database")
    

    # Base.metadata.drop_all(bind=engine)
    
    Base.metadata.create_all(bind=engine)
    

if __name__ == "__main__":
    setup_database()