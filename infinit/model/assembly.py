"""Assembly model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String

from infinit.model.meta import Base

class Assembly(Base):
    __tablename__ = "assembly"

    id = Column(Integer, primary_key=True)

    name = Column(String(100))
    description = Column(String(100))


    def __init__(self, name='', description=''):
        self.description=description;
        self.name=name;

    def __repr__(self):
        return "Assembly('%s')" % self.name