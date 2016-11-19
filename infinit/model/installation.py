"""Installation model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime

from infinit.model.meta import Base

class Installation(Base):
    __tablename__ = "Installation"

    id = Column(Integer, primary_key=True)
    part_id = Column(Integer, ForeignKey('part.id'))
    assembly_id = Column(Integer, ForeignKey('assembly.id'))

    start = Column(DateTime)
    end = Column(DateTime)

    def __init__(self, part_id=0, assembly_id=0, description='', start=None, end=None):
        self.part_id=part_id
        self.assembly_id=assembly_id
        self.start=start;
        self.end=end;

    def __repr__(self):
        return "Installation('%s')" % self.name