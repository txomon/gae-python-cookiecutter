from setuptools import setup, find_packages


def load_reqs(file_name):
    with open(file_name) as fd:
        return fd.readlines()

def load_version(file_name):
    with open(file_name) as fd:
        for line in fd:
            if '__version__' in line:
                version_string = line.split('=')[1]
                return version_string.replace('\'"', '')


setup(
    name='{{cookiecutter.project_slug}}',
    version=load_version('{{cookiecutter.project_slug}}/__init__.py'),
    description='{{cookiecutter.project_short_description}}',
    author_name='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    packages=find_packages(exclude=['lib/']),
    install_requires=load_reqs('requirements.txt'),
    tests_require=load_reqs('test-requirements.txt')
)
