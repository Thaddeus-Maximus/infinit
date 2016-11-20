# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479617374.563
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
        revisions = context.get('revisions', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n<h1>Component: ')
        __M_writer(escape(component.name))
        __M_writer(u'</h1>\r\n<table>\r\n\t<thead>\r\n\t\t<tr>\r\n\t\t\t<td>\r\n\t\t\t\tRevision\r\n\t\t\t</td><td>\r\n\t\t\t\tPart\r\n\t\t\t</td>\r\n\t\t</tr>\r\n\t</thead>\r\n')
        for revision in revisions:
            __M_writer(u'\t  \t<tr>\r\n\t  \t\t<td>\r\n\t  \t\t\t<a href="/view/revision/')
            __M_writer(escape(revision.id))
            __M_writer(u'">')
            __M_writer(escape(revision.name))
            __M_writer(u'</a>\r\n\t  \t\t</td>\r\n')
            for part in revision.parts:
                __M_writer(u'\t  \t\t\t<td>\r\n\t  \t\t\t\t<a href="/view/part/')
                __M_writer(escape(part.id))
                __M_writer(u'">#')
                __M_writer(escape(part.id))
                __M_writer(u'</a>\r\n\t  \t\t\t</td>\r\n')
            __M_writer(u'\t  \t</tr>\r\n')
        __M_writer(u'</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 16, "33": 18, "34": 19, "35": 20, "36": 20, "37": 20, "38": 20, "39": 23, "40": 25, "46": 40, "17": 0, "24": 1, "25": 2, "26": 2, "27": 13, "28": 14, "29": 16, "30": 16, "31": 16}, "uri": "/view_component.html", "filename": "D:/EngineeringWorkspace/Infinit/infinit/templates/view_component.html"}
__M_END_METADATA
"""
