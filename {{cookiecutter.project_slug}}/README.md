{{cookiecutter.project_name}}
{{ '='*len(cookiecutter.project_name) }}

{{cookiecutter.project_short_description}}

API
---

There is a simple API available. First of all, httplib has been wrapped in
`http_request` function to ease of use.

`gen_ok` and `gen_err` functions have been generated to ease the creation
of flask responses

`Return` exception can be raised if one wants to answer something to the
request

`get_memcached` function has been created to ease compatibility between
standard and flexible environments

When coding, you SHOULD NOT use any `google` namespace import.


Testing
-------

To test this, one should be using an sh compatible shell that support
`$(some command)` and `export ENV_VAR=` syntax.

Finally, tests are run using `tox`.

### Memcached

Memcached can be booted locally by just running `memcached`, the default
configuration for this project allows to seamlessly integrate with vanilla
memcached

### Datastore

Datastore can be booted locally through `gcloud beta emulators datastore 
start`. In this case however, one should initialize the environment, for
example by running `$(gcloud beta emulators datastore env-init)`.
