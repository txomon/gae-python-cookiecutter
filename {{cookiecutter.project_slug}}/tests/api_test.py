def test_root_api(api_client):
    status_code, body, _ = api_client.get('/')
    assert 200 == status_code
    assert 'API' in body
    assert {{cookiecutter.project_short_description}} == body['API']
