# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479617624.662
_enable_loop = True
_template_filename = 'D:/EngineeringWorkspace/Infinit/infinit/templates/view_revision.html'
_template_uri = '/view_revision.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        r = context.get('r', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u"\r\n<h1>Revision: <a href='/view/component/")
        __M_writer(escape(r.component_id))
        __M_writer(u"'>")
        __M_writer(escape(r.component.name))
        __M_writer(u'</a> - ')
        __M_writer(escape(r.name))
        __M_writer(u'</h1>\r\n<p>')
        __M_writer(escape(r.description))
        __M_writer(u'</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"37": 31, "17": 0, "23": 1, "24": 2, "25": 2, "26": 2, "27": 2, "28": 2, "29": 2, "30": 3, "31": 3}, "uri": "/view_revision.html", "filename": "D:/EngineeringWorkspace/Infinit/infinit/templates/view_revision.html"}
__M_END_METADATA
"""
