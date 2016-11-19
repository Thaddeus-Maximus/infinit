"""The application's model objects"""
from infinit.model.meta import Session, Base
import assembly
import component
import event
import installation
import meta
import part
import revision


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
