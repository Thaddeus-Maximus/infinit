# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479663939.498
_enable_loop = True
_template_filename = 'D:/EngineeringWorkspace/Infinit/infinit/templates/view_component.html'
_template_uri = '/view_component.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        component = context.get('component', UNDEFINED)
        len = context.get('len', UNDEFINED)
        revisions = context.get('revisions', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<h1>Component: ')
        __M_writer(escape(component.name))
        __M_writer(u'</h1>\r\n<div class="uk-panel uk-panel-box uk-panel-box-primary">\r\n  <h3>Description:</h3>\r\n  <p class="uk-text-primary">')
        __M_writer(escape(component.description))
        __M_writer(u'</p>\r\n</div>\r\n\r\n')
        if len(component.revisions) > 0:
            __M_writer(u'  <table class="uk-table uk-table-striped uk-table-hover uk-table-condensed">\r\n    <caption>Revisions of this component</caption>\r\n    <thead>\r\n      <tr>\r\n        <th>\r\n          Revision\r\n        </th>\r\n        <th>\r\n          Description\r\n        </th>\r\n        <th>\r\n          Parts\r\n        </th>\r\n      </tr>\r\n    </thead>\r\n')
            for revision in revisions:
                __M_writer(u'      <tr onclick="window.document.location=\'/view/revision/')
                __M_writer(escape(revision.id))
                __M_writer(u'\';">\r\n        <td>\r\n          <a>')
                __M_writer(escape(revision.name))
                __M_writer(u'</a>\r\n        </td>\r\n        <td>\r\n          <a>')
                __M_writer(escape( (revision.description[:18] + '..') if len(revision.description) > 20 else revision.description))
                __M_writer(u'</a>\r\n        </td>\r\n        \r\n        <td>\r\n')
                for part in revision.parts:
                    __M_writer(u'          \r\n            <a href="/view/part/')
                    __M_writer(escape(part.id))
                    __M_writer(u'">#')
                    __M_writer(escape(part.id))
                    __M_writer(u'</a>\r\n          \r\n')
                __M_writer(u'        </td>\r\n      </tr>\r\n')
            __M_writer(u'  </table>\r\n')
        else:
            __M_writer(u'  <div class="uk-alert uk-alert-warning">No revisions were found for this component.</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "25": 1, "26": 1, "27": 1, "28": 4, "29": 4, "30": 7, "31": 8, "32": 23, "33": 24, "34": 24, "35": 24, "36": 26, "37": 26, "38": 29, "39": 29, "40": 33, "41": 34, "42": 35, "43": 35, "44": 35, "45": 35, "46": 38, "47": 41, "48": 42, "49": 43, "55": 49}, "uri": "/view_component.html", "filename": "D:/EngineeringWorkspace/Infinit/infinit/templates/view_component.html"}
__M_END_METADATA
"""
