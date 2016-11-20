# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479665208.294
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
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u"\r\n<h1>Revision: <a href='/view/component/")
        __M_writer(escape(r.component_id))
        __M_writer(u"'>")
        __M_writer(escape(r.component.name))
        __M_writer(u'</a> - ')
        __M_writer(escape(r.name))
        __M_writer(u'</h1>\r\n<div class="uk-panel uk-panel-box uk-panel-box-primary">\r\n  <h3>Description:</h3>\r\n  <p class="uk-text-primary">')
        __M_writer(escape(r.description))
        __M_writer(u'</p>\r\n</div>\r\n<br/>\r\n<div class="uk-panel uk-panel-box">\r\n  <h3>Component Description:</h3>\r\n  <p class="uk-text-primary">')
        __M_writer(escape(r.component.description))
        __M_writer(u'</p>\r\n</div>\r\n\r\n')
        if len(r.parts) > 0:
            __M_writer(u'  <table class="uk-table uk-table-striped uk-table-hover uk-table-condensed">\r\n    <caption>Parts of this revision</caption>\r\n    <thead>\r\n      <tr>\r\n        <th>\r\n          Part\r\n        </th><th>\r\n          Description\r\n        </th><th>\r\n          Drive Hours\r\n        </th><th>\r\n          Status\r\n        </th><th>\r\n          Events\r\n        </th>\r\n      </tr>\r\n    </thead>\r\n')
            for part in r.parts:
                __M_writer(u'      <!--')
                __M_writer(escape(part.computeEvents()))
                __M_writer(u'-->\r\n      <tr onclick="window.document.location=\'/view/part/')
                __M_writer(escape(part.id))
                __M_writer(u'\';">\r\n        <td>\r\n          <a>#')
                __M_writer(escape(part.id))
                __M_writer(u'</a>\r\n        </td>\r\n        <td>\r\n          <a>')
                __M_writer(escape((part.description[:18] + '..') if len(part.description) > 20 else part.description))
                __M_writer(u'</a>\r\n        </td>\r\n        <td>\r\n          ')
                __M_writer(escape("{0:.1f}".format(part.drive_time.total_seconds()/3600)))
                __M_writer(u'\r\n        </td>\r\n        <td>\r\n          <!--Status-->\r\n        </td>\r\n        <td>\r\n')
                for event in part.total_events:
                    __M_writer(u'          \r\n            <a href="/view/event/')
                    __M_writer(escape(event.id))
                    __M_writer(u'">')
                    __M_writer(escape((event.description[:18] + '..') if len(event.description) > 20 else event.description))
                    __M_writer(u'</a>\r\n          \r\n')
                __M_writer(u'        </td>\r\n      </tr>\r\n')
            __M_writer(u'  </table>\r\n')
        else:
            __M_writer(u'  <div class="uk-alert uk-alert-warning">No parts were found for this revision.</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 2, "26": 2, "27": 2, "28": 2, "29": 2, "30": 2, "31": 5, "32": 5, "33": 10, "34": 10, "35": 13, "36": 14, "37": 31, "38": 32, "39": 32, "40": 32, "41": 33, "42": 33, "43": 35, "44": 35, "45": 38, "46": 38, "47": 41, "48": 41, "49": 47, "50": 48, "51": 49, "52": 49, "53": 49, "54": 49, "55": 52, "56": 55, "57": 56, "58": 57, "64": 58}, "uri": "/view_revision.html", "filename": "D:/EngineeringWorkspace/Infinit/infinit/templates/view_revision.html"}
__M_END_METADATA
"""
