from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}}.restutils import gen_error, gen_ok



def root_get():
    return gen_ok({'API': '{{cookiecutter.project_name}}', 'version': __version__ })


def error_404(e):
    error, code, headers = gen_error(message='Endpoint not found', code=404)
    return error, code, headers


def error_405(*args, **kwargs):
    error, code, headers = gen_error(message='Method not allowed', code=405)
    return error, code, headers


def error_500(e):
    error, code, headers = gen_error(
        message='Server is running in problems, contact'
        '{{cookiecutter.email}} if problem persists',
        code=500)
    return error, code, headers
