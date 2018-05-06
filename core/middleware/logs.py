# -*- coding: utf-8 -*-

import logging
from django.utils.deprecation import MiddlewareMixin

log = logging.getLogger('info')


# 新版的 Django 中间层要继承 MiddlewareMixin
class LogMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        try:
            # multipart/form-data 表示的是二进制的文件
            if request.environ["CONTENT_TYPE"].find("multipart/form-data") < 0:
                body = request.body.decode('utf-8')
            else:
                body = ''
        except Exception as e:
            body = str(e)
        log.info('\n<Request>'
                 '\n[METHOD]:{method}'
                 '\n[URL   ]:{url}'
                 '\n[TOKEN ]:{token}'
                 '\n[BODY  ]:{body}\n'
                 .format(method=request.method,
                         url=request.get_full_path(),
                         token=request.environ.get("HTTP_TOKEN"),
                         body=body)
                 )

    @staticmethod
    def process_response(request, response):
        try:
            if request.environ["CONTENT_TYPE"].find("multipart/form-data") >= 0:
                body = ""
            else:
                body = request.body.decode('utf-8')

            body = body[:20] if len(body) > 20 else body
        except Exception as e:
            body = str(e)
        try:
            content = response.content.decode('utf-8')
        except Exception as e:
            content = str(e)

        log.info('\n<Request & RESPONSE>'
                 '\n[METHOD]:{method}'
                 '\n[URL   ]:{url}'
                 '\n[TOKEN ]:{token}'
                 '\n[BODY  ]:{body}'
                 '\n[STATUS_CODE]:{status_code}'
                 '\n[RESPONSE]:{response}\n'
                 .format(method=request.method,
                         url=request.get_full_path(),
                         token=request.environ.get("HTTP_TOKEN"),
                         body=body,
                         status_code=response.status_code,
                         response=content[:20])
                 )
        return response
