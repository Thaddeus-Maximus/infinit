import cgi

from paste.urlparser import PkgResourcesParser
from pylons.middleware import error_document_template
from webhelpers.html.builder import literal

from sqlalchemy.orm.exc import NoResultFound

from infinit.lib.base import BaseController

from infinit.model import meta
from infinit.model.revision import * 
from infinit.model.part import * 
from infinit.model.component import * 

from pylons.templating import render_mako as render

class ViewController(BaseController):
  def index(self, **kwargs):
    # diffmount = component.Component()
    # diffmount.name = '006-DT-P45'
    # meta.Session.add(diffmount)
    # meta.Session.commit()
    if kwargs['type'] == 'component':
      try:
        query = meta.Session.query(Component)
        component = query.filter(Component.id==kwargs['id']).one()
        

        return render('/layout.html', extra_vars={'content':render('/view_component.html', extra_vars={'component': component, 'revisions':component.revisions})})
      except NoResultFound:
        return 'No component found!'
    
    elif kwargs['type'] == 'revision':
      try:
        query = meta.Session.query(Revision)
        revision = query.filter(Revision.id==kwargs['id']).one()

        return render('/layout.html', extra_vars={'content':render('/view_revision.html', extra_vars={'r': revision})})
      except NoResultFound:
        return 'No revision found!'
    
    elif kwargs['type'] == 'part':
      try:
        query = meta.Session.query(Part)
        part = query.filter(Part.id==kwargs['id']).one()
        part.computeEvents()

        return repr(part.total_events); #render('/view_part.html', extra_vars={'r': revision})
      except NoResultFound:
        return 'No part found!'