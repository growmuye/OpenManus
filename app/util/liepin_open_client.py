# -*- coding: utf-8 -*-

import json
from datetime import datetime
import hashlib
from urllib.parse import urlparse

from requests import Session, Request

import hmac
import base64


# access open api client demo
class LiepinOpenClient:

    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret

    def gen_sign_str(self, method, url, content_type, headers, params):

        accept = headers.get('accept')
        timestamp = headers.get('x-alt-timestamp')

        sign_string = ''
        content_md5 = None
        if (params is not None) and (content_type.lower().startswith('application/json')):
            content_md5 = base64.urlsafe_b64encode(hashlib.md5(json.dumps(params).encode('utf8')).digest()).decode(
                'utf8')
        path_and_params = urlparse(url).path
        form_params = {}
        for item in urlparse(url).query.split('&'):
            if item == '':
                continue
            kv = item.split('=')
            form_params[kv[0]] = kv[1]
        if content_type is not None and content_type.lower().startswith(
                'application/x-www-form-urlencoded') and params is not None:
            form_params.update(params)
        form_params_str = ''
        for k, v in sorted(form_params.items()):
            form_params_str += k + '=' + v + '&'
        if form_params_str.endswith('&'):
            form_params_str = form_params_str[:-1]
        if len(form_params_str) > 0:
            path_and_params += '?' + form_params_str

        sign_string += 'x-alt-timestamp: ' + timestamp + '\n'

        sign_string += method + '\n'

        sign_string += accept + '\n'

        if content_type is not None:
            sign_string += content_type + '\n'
        else:
            sign_string += '\n'

        if content_md5 is not None:
            sign_string += content_md5 + '\n'
        else:
            sign_string += '\n'

        sign_string += path_and_params

        # print('sign_string=' + sign_string)

        return sign_string

    def sign(self, method, url, content_type, headers, params):
        key = self.app_secret.encode('utf-8')
        sgn_str = self.gen_sign_str(method, url, content_type, headers, params).encode('utf-8')
        base64.urlsafe_b64encode(hmac.new(base64.b64decode(key), sgn_str, digestmod=hashlib.sha256).digest())
        dgst = hmac.new(key, sgn_str, digestmod=hashlib.sha256).digest()
        sign = base64.urlsafe_b64encode(dgst)
        sign = str(sign, 'utf-8')
        headers[
            'Authorization'] = 'app key="%s", algorithm="HmacSHA256", headers="x-alt-timestamp", signature="%s"' % (
            self.app_key, sign)
        return sign

    def send(self, method, url, content_type=None, params=None):
        headers = {'x-alt-timestamp': str(int(datetime.timestamp(datetime.now()) * 1000)),
                   'accept': 'application/json'}
        if content_type is not None:
            headers['content-type'] = content_type
        self.sign(method, url, content_type, headers, params)
        # print('req_headers=' + str(headers))
        with Session() as s:
            req = None
            if method.lower() == 'post':
                if params is not None and content_type.lower().startswith('application/json'):
                    req = Request(method=method, url=url, json=params, headers=headers)
                if params is not None and content_type.lower().startswith('application/x-www-form-urlencoded'):
                    req = Request(method=method, url=url, data=params, headers=headers)
                if params is None:
                    raise Exception('content-type is not supported')
            else:
                req = Request(method=method, url=url, headers=headers)

            prepped = s.prepare_request(req)
            response = s.send(prepped)
            return response

