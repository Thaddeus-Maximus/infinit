"""Part model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship

from infinit.model.meta import Base

from datetime import timedelta

class Part(Base):
  __tablename__ = "part"

  id = Column(Integer, primary_key=True)
  revision_id = Column(Integer, ForeignKey('revision.id'))

  description = Column(String(100))

  revision = relationship("Revision", lazy='joined')
  installations = relationship("Installation", lazy='joined')
  events = relationship("Event", lazy='joined')

  def computeEvents(self):
    self.total_events = self.events
    self.drive_time = timedelta(0)
    for event in self.events:
      self.drive_time = self.drive_time + event.end - event.start
    for installation in self.installations:
      for event in installation.assembly.events:
        if (event.start >= installation.start and event.end <= installation.end):
          self.total_events.append(event)
          self.drive_time = self.drive_time + event.end - event.start



  def __init__(self, revision_id=0, description=''):
    self.revision_id=revision_id
    self.description=description

  def __repr__(self):
    return "Part('%s')" % self.id