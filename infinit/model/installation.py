"""Installation model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.orm import relationship

from infinit.model.meta import Base

class Installation(Base):
    __tablename__ = "Installation"

    id = Column(Integer, primary_key=True)
    part_id = Column(Integer, ForeignKey('part.id'))
    assembly_id = Column(Integer, ForeignKey('assembly.id'))

    start = Column(DateTime)
    end = Column(DateTime)

    assembly = relationship("Assembly", lazy='joined')
    part = relationship("Part", lazy='joined')

    def __init__(self, part_id=0, assembly_id=0, description='', start=None, end=None):
        self.part_id=part_id
        self.assembly_id=assembly_id
        self.start=start;
        self.end=end;

    def __repr__(self):
        return "Installation(%s->%s #%s)" % (self.part_id, self.assembly_id, self.id)