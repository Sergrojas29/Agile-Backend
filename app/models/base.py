from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
    # def to_dict(self):
    #     data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    #     data.pop("password", None) ## keeping passwords secure - they are not returned 
    #     return data
    