# -*- coding: utf-8 -*-

import logging
from django.utils.deprecation import MiddlewareMixin

log = logging.getLogger('info')


class LogMiddleware(MiddlewareMixin):

    @staticmethod
    def process_response(request, response):
        visible_types = {'application/json', 'text/plain', 'text/html', 'text/xml'}

        ct = request.content_type
        body = request.body
        try:
            if ct in visible_types:
                body = body.decode('utf-8')
            else:
                body = body[:20] if body else 'None'
        except Exception as e:
            body = str(e)

        try:
            content = response.content.decode('utf-8')
            content = content[:20] if content else 'None'
        except Exception as e:
            content = str(e)

        info = '<request> "{method} {url}" "{content_type}" {status} \nbody: {body} \n{content}'.format(
            method=request.method, url=request.get_full_path(), content_type=ct, status=response.status_code,
            body=body, content=content
        )
        log.info(info)

        return response
