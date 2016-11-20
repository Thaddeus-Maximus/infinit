# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479592202.488
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
        __M_writer(u'<html>\r\n<head>\r\n    <title>Infinit - ')
        __M_writer(escape(r.name))
        __M_writer(u'</title>\r\n</head>\r\n<body>\r\n    <h1>r: ')
        __M_writer(escape(r.name))
        __M_writer(u'</h1>\r\n    <p>')
        __M_writer(escape(r.description))
        __M_writer(u'</p>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"35": 29, "17": 0, "23": 1, "24": 3, "25": 3, "26": 6, "27": 6, "28": 7, "29": 7}, "uri": "/view_revision.html", "filename": "D:/EngineeringWorkspace/Infinit/infinit/templates/view_revision.html"}
__M_END_METADATA
"""
