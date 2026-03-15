from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# ! update to move to config or .env
DATABASE_URL = "postgresql://postgres:0415@localhost:5432/postgres"

# Creat Enginge ONCE
engine = create_engine(DATABASE_URL, echo=False)

# Create A session Factory
SessionLocal = sessionmaker(bind=engine)

# # 4. Your Base class
# class Base(DeclarativeBase):
#     pass


class Base(DeclarativeBase):
    def to_dict(self):
        """SQLAchemy model to a dict - so we dont haqve to jsonify the object """
        return{
            c.name: getattr(self, c.name) for c in self.__table___.columns
        }