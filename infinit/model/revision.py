"""Revision model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship

from infinit.model.meta import Base

class Revision(Base):
    __tablename__ = "revision"

    id = Column(Integer, primary_key=True)
    component_id = Column(Integer, ForeignKey('component.id'))
    
    name = Column(String(100))

    description = Column(String(100))

    parts = relationship("Part", lazy='joined')


    def __init__(self, component_id=0, name=0, description='', start=None, end=None):
        self.component_id=component_id
        self.name=name
        self.description=description;

    def __repr__(self):
        return "Revision('%s')" % self.name