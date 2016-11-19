import cgi

from paste.urlparser import PkgResourcesParser
from pylons.middleware import error_document_template
from webhelpers.html.builder import literal

from infinit.lib.base import BaseController

class PartController(BaseController):
    """Generates error documents as and when they are required.

    The ErrorDocuments middleware forwards to ErrorController when error
    related status codes are returned from the application.

    This behaviour can be altered by changing the parameters to the
    ErrorDocuments middleware in your config/middleware.py file.

    """
    def index(self, **kwargs):
        return 'whoa nelly' + str(kwargs)