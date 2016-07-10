import pytest

from {{cookiecutter.project_slug}}.server import get_app()

@pytest.fixture
def test_app_client():
    app = get_app()
    return app.test_client()


@pytest.fixture
def app_client(test_app_client):
    def add_json(kwargs):
        if 'json' in kwargs:
            json_obj = kwargs.pop('json')
            kwargs['data'] = json.dumps(json_obj)
            headers = kwargs.pop('headers', {})
            headers['Content-Type'] = 'application/json'
            kwargs['headers'] = headers

    class AppClient(object):
        def get(url, **kwargs):
            response = test_app_client.get(url, **kwargs)
            status_code = response.status_code
            body = response.data
            body = json.loads(body)
            headers = response.headers
            return status_code, body, headers

        def post(url, **kwargs):
            add_json(kwargs)
            response = test_app_client.post(url, **kwargs)
            status_code = response.status_code
            body = response.data
            body = json.loads(body)
            headers = response.headers
            return status_code, body, headers


        def put(url, **kwargs):
            add_json(kwargs)
            response = test_app_client.put(url, **kwargs)
            status_code = response.status_code
            body = response.data
            body = json.loads(body)
            headers = response.headers
            return status_code, body, headers


        def patch(url, **kwargs):
            add_json(kwargs)
            response = test_app_client.patch(url, **kwargs)
            status_code = response.status_code
            body = response.data
            body = json.loads(body)
            headers = response.headers
            return status_code, body, headers


        def delete(url, **kwargs):
            add_json(kwargs)
            response = test_app_client.delete(url, **kwargs)
            status_code = response.status_code
            body = response.data
            body = json.loads(body)
            headers = response.headers
            return status_code, body, headers

    return AppClient()
