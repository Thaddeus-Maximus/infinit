# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479617527.591
_enable_loop = True
_template_filename = 'D:/EngineeringWorkspace/Infinit/infinit/templates/layout.html'
_template_uri = '/layout.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        content = context.get('content', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n<html>\r\n<head>\r\n<link rel="stylesheet" href="/css/uikit.css">\r\n</head>\r\n<body>\r\n<div class="uk-container">\r\n<nav class="uk-navbar uk-margin-large-bottom">\r\n    <a class="uk-navbar-brand uk-hidden-small" href="layouts_frontpage.html">Infinit</a>\r\n    <ul class="uk-navbar-nav uk-hidden-small">\r\n        <li>\r\n            <a href="layouts_frontpage.html">Parts</a>\r\n        </li>\r\n        <li>\r\n            <a href="layouts_portfolio.html">Assemblies</a>\r\n        </li>\r\n        <li>\r\n            <a href="layouts_blog.html">Events</a>\r\n        </li>\r\n    </ul>\r\n    <a href="#offcanvas" class="uk-navbar-toggle uk-visible-small" data-uk-offcanvas></a>\r\n    <div class="uk-navbar-brand uk-navbar-center uk-visible-small">Brand</div>\r\n</nav>\r\n\r\n')
        __M_writer(escape(content))
        __M_writer(u'\r\n\r\n</div>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"24": 25, "17": 0, "31": 25, "25": 25, "23": 1}, "uri": "/layout.html", "filename": "D:/EngineeringWorkspace/Infinit/infinit/templates/layout.html"}
__M_END_METADATA
"""
