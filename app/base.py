from sqlalchemy.orm import DeclarativeBase 

class Base(DeclarativeBase):
    def to_dict(self):
        """SQLAchemy model to a dict - so we dont haqve to jsonify the object """
        return{
            c.name: getattr(self, c.name) for c in self.__table___.columns
        }