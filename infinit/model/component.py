"""Component model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship
from infinit.model.meta import Base

class Component(Base):
    __tablename__ = "component"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(100))
    revisions = relationship("Revision", lazy='joined')

    def __init__(self, name='', description=''):
        self.name = name
        self.description = description

    def __repr__(self):
        return "Component('%s')" % self.name