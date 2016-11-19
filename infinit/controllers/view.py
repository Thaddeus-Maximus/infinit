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
        component_query = meta.Session.query(Component)
        component = component_query.filter(Component.id==kwargs['id']).one()
        # find parts


        return render('/view.html', extra_vars={'component': component, 'revisions':component.revisions})
      except NoResultFound:
        return 'No component found!'
      