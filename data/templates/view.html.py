# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479588311.541
_enable_loop = True
_template_filename = 'D:/EngineeringWorkspace/Infinit/infinit/templates/view.html'
_template_uri = '/view.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        component = context.get('component', UNDEFINED)
        revisions = context.get('revisions', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\r\n<head>\r\n    <title>Infinit - ')
        __M_writer(escape(component.name))
        __M_writer(u'</title>\r\n</head>\r\n<body>\r\n    <h1>Component: ')
        __M_writer(escape(component.name))
        __M_writer(u'</h1>\r\n    <table>\r\n    \t<thead>\r\n    \t\t<tr>\r\n    \t\t\t<td>\r\n    \t\t\t\tRevision\r\n    \t\t\t</td><td>\r\n    \t\t\t\tPart\r\n    \t\t\t</td>\r\n    \t\t</tr>\r\n    \t</thead>\r\n')
        for revision in revisions:
            __M_writer(u'    \t  \t<tr>\r\n    \t  \t\t<td>\r\n    \t  \t\t\t<a href="/view/revision/')
            __M_writer(escape(revision.id))
            __M_writer(u'">')
            __M_writer(escape(revision.name))
            __M_writer(u'</a>\r\n    \t  \t\t</td>\r\n')
            for part in revision.parts:
                __M_writer(u'    \t  \t\t\t<td>\r\n    \t  \t\t\t\t<a href="/view/part/')
                __M_writer(escape(part.id))
                __M_writer(u'">#')
                __M_writer(escape(part.id))
                __M_writer(u'</a>\r\n    \t  \t\t\t</td>\r\n')
            __M_writer(u'    \t  \t</tr>\r\n')
        __M_writer(u'    </table>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 20, "33": 20, "34": 20, "35": 22, "36": 23, "37": 24, "38": 24, "39": 24, "40": 24, "41": 27, "42": 29, "48": 42, "17": 0, "24": 1, "25": 3, "26": 3, "27": 6, "28": 6, "29": 17, "30": 18, "31": 20}, "uri": "/view.html", "filename": "D:/EngineeringWorkspace/Infinit/infinit/templates/view.html"}
__M_END_METADATA
"""
