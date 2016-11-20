# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479665159.884
_enable_loop = True
_template_filename = 'D:/EngineeringWorkspace/Infinit/infinit/templates/view_part.html'
_template_uri = '/view_part.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        part = context.get('part', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u"<h1>\r\n  Part:\r\n  <a href='/view/component/")
        __M_writer(escape(part.revision.component.id))
        __M_writer(u"'>")
        __M_writer(escape(part.revision.component.name))
        __M_writer(u"</a>\r\n  - <a href='/view/revision/")
        __M_writer(escape(part.revision.id))
        __M_writer(u"'>")
        __M_writer(escape(part.revision.name))
        __M_writer(u'</a>\r\n  - #')
        __M_writer(escape(part.id))
        __M_writer(u'\r\n</h1>\r\n\r\n<div class="uk-panel uk-panel-box uk-panel-box-primary">\r\n  <h3>Description:</h3>\r\n  <p class="uk-text-primary">')
        __M_writer(escape(part.description))
        __M_writer(u'</p>\r\n</div>\r\n\r\n')
        if len(part.installations) > 0:
            __M_writer(u'  <table class="uk-table uk-table-striped uk-table-hover uk-table-condensed">\r\n    <caption>Installations</caption>\r\n    <thead>\r\n      <tr>\r\n        <th>\r\n          Assembly\r\n        </th><th>\r\n          Date On\r\n        </th><th>\r\n          Date Off\r\n        </th><th>\r\n          Description\r\n        </th>\r\n      </tr>\r\n    </thead>\r\n')
            for installation in part.installations:
                __M_writer(u'      <tr onclick="window.document.location=\'/view/event/')
                __M_writer(escape(installation.id))
                __M_writer(u'\';">\r\n        <td>\r\n          <a href=\'/view/assembly/')
                __M_writer(escape(installation.assembly.id))
                __M_writer(u"'>")
                __M_writer(escape(installation.assembly.name))
                __M_writer(u'</a>\r\n        </td>\r\n\r\n        <td>\r\n          ')
                __M_writer(escape(installation.start))
                __M_writer(u'\r\n        </td>\r\n        <td>\r\n          ')
                __M_writer(escape(installation.end))
                __M_writer(u'\r\n        </td>\r\n\r\n        <td>\r\n          <a>')
                __M_writer(escape( (installation.description[:18] + '..') if len(installation.description) > 20 else installation.description))
                __M_writer(u'</a>\r\n        </td>\r\n      </tr>\r\n')
            __M_writer(u'  </table>\r\n')
        else:
            __M_writer(u'  <div class="uk-alert uk-alert-warning">No installations were found for this revision.</div>\r\n')
        __M_writer(u'\r\n\r\n')
        if len(part.total_events) > 0:
            __M_writer(u'  <table class="uk-table uk-table-striped uk-table-hover uk-table-condensed">\r\n    <caption>Events</caption>\r\n    <thead>\r\n      <tr>\r\n        <th>\r\n          ID\r\n        </th><th>\r\n          Date\r\n        </th><th>\r\n          Description\r\n        </th><th>\r\n          Drive Hours\r\n        </th>\r\n      </tr>\r\n    </thead>\r\n')
            for event in part.total_events:
                __M_writer(u'      <tr onclick="window.document.location=\'/view/event/')
                __M_writer(escape(event.id))
                __M_writer(u'\';">\r\n        <td>\r\n          <a>#')
                __M_writer(escape(event.id))
                __M_writer(u'</a>\r\n        </td>\r\n\r\n        <td>\r\n          ')
                __M_writer(escape(event.start))
                __M_writer(u'\r\n        </td>\r\n\r\n        <td>\r\n          <a>')
                __M_writer(escape( (event.description[:18] + '..') if len(event.description) > 20 else event.description))
                __M_writer(u'</a>\r\n        </td>\r\n        \r\n        \r\n\r\n        <td>\r\n')
                if event.end!=None and event.start!=None and event.end != event.start:
                    __M_writer(u'            ')
                    __M_writer(escape( "{0:.1f}".format((event.end-event.start).total_seconds() /3600) ))
                    __M_writer(u'\r\n')
                __M_writer(u'        </td>\r\n      </tr>\r\n')
            __M_writer(u'  </table>\r\n')
        else:
            __M_writer(u'  <div class="uk-alert uk-alert-warning">No events were found for this revision.</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 3, "26": 3, "27": 3, "28": 3, "29": 4, "30": 4, "31": 4, "32": 4, "33": 5, "34": 5, "35": 10, "36": 10, "37": 13, "38": 14, "39": 29, "40": 30, "41": 30, "42": 30, "43": 32, "44": 32, "45": 32, "46": 32, "47": 36, "48": 36, "49": 39, "50": 39, "51": 43, "52": 43, "53": 47, "54": 48, "55": 49, "56": 51, "57": 53, "58": 54, "59": 69, "60": 70, "61": 70, "62": 70, "63": 72, "64": 72, "65": 76, "66": 76, "67": 80, "68": 80, "69": 86, "70": 87, "71": 87, "72": 87, "73": 89, "74": 92, "75": 93, "76": 94, "82": 76}, "uri": "/view_part.html", "filename": "D:/EngineeringWorkspace/Infinit/infinit/templates/view_part.html"}
__M_END_METADATA
"""
