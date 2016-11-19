"""Part model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String

from infinit.model.meta import Base

class Part(Base):
    __tablename__ = "part"

    id = Column(Integer, primary_key=True)
    revision_id = Column(Integer, ForeignKey('revision.id'))

    description = Column(String(100))

    def __init__(self, revision_id=0, description=''):
        self.revision_id=revision_id
        self.description=description

    def __repr__(self):
        return "Part('%s')" % self.id