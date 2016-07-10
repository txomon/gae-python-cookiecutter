import httplib
import json as _json
import logging
import os
import uuid
from urlparse import urlsplit, SplitResult

from pymemcache.client import Client as Memcached
from six.moves.urllib.parse import urlencode

logger = logging.getLogger()

_memcached = None


def get_memcached():
    global _memcached
    if _memcached:
        return _memcached
    try:
        from google.appengine.api import memcache as mc
        _memcached = mc
        logger.info('Configuring memcached as in standard env')
        return _memcached
    except:
        logger.info('Configuring memcached as in flexible env')
    memcache_addr = os.environ.get('MEMCACHE_PORT_11211_TCP_ADDR', 'localhost')
    memcache_port = os.environ.get('MEMCACHE_PORT_11211_TCP_PORT', 11211)
    _memcached = Memcached((memcache_addr, int(memcache_port)))
    return _memcached


def gen_error(obj=None, message='', code=400):
    if not obj:
        obj = {}
    res = {
        '_status': 'ERR',
        '_error': {'code': code, 'message': message}
    }
    res.update(obj)
    return _json.dumps(res), code, {'Content-Type': 'application/json'}


def gen_ok(obj=None, code=200):
    obj['_status'] = 'OK'
    return _json.dumps(obj), code, {'Content-Type': 'application/json'}


class Return(Exception):
    def __init__(self, message='', code=400, obj=None):
        if obj is None:
            self.obj = {}
        else:
            self.obj = obj
        self.code = code
        super(Return, self).__init__(message)


def return_error(e):
    return gen_error(e.obj, e.message, e.code)


def http_request(method, url, data=None, json=None, headers=None):
    body = None
    if not headers:
        headers = {}
    if json and isinstance(json, dict):
        headers['Content-Type'] = 'application/json'
        body = _json.dumps(json)
    elif data and isinstance(data, dict):
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        body = urlencode(data)
    if method not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        raise Exception('Method %s is not supported' % method)
    try:
        parsed_url = urlsplit(url)
        assert isinstance(parsed_url, SplitResult)
        if parsed_url.scheme == 'https':
            connection = httplib.HTTPSConnection
        elif parsed_url.scheme == 'http':
            connection = httplib.HTTPConnection
        conn = connection(parsed_url.netloc)
        conn.request(
            method,
            '{}?{}'.format(parsed_url.path, parsed_url.query),
            body,
            headers
        )
        res = conn.getresponse()
        res_headers = dict(res.getheaders())
        res_code = res.status
        res_body = res.read()
    except Exception:
        logger.exception('Something happened while processing the request')
        raise Exception('Http request failed')
    return res_body, res_code, res_headers
