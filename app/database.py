from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os 
from dotenv import load_dotenv 

# load the env 
load_dotenv()
DATABASE_URL: str = os.getenv("DATABASE_URL")

# Creat Engine ONCE
engine = create_engine(DATABASE_URL, echo=False)

# Create A session Factory
SessionLocal = sessionmaker(bind=engine)


