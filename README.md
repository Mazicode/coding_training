---
title: 'geoservice'
---

[![ci](https://github.com/Mazicode/coding_challenge)]

Requirements
============

-   Python 3.7.0
-   Docker

Workflow
-------------
``` {.sourceCode .bash}
# the app consists of one main function that runs within a flask instance 
to display the results of some coordinates/locations conversions.
The geo data conversion is taken care by an async function called 'transform' that receives inputs locally:
the input data is provided by the utils module, which feeds the async function with such inputs and
also takes care of strings recognition, telling whether the input is a coordinate, an actual location or 
none of the mentioned.
The user is expected to view a json list of objects as value pairs (before and after conversion).
```

Development Setup
=================

In general, the following steps can be your guide for setting a local
development environment:

``` {.sourceCode .bash}
# Clone the repository and cd into it
$ git clone {https://github.com/Mazicode/coding_challenge}

# Create your virtualenv, using pyenv for example (highly recommended: https://github.com/pyenv/pyenv)
$ pyenv virtualenv 3.7.0 virtual_env

# From within the root directory and with an active virtualenv, install the dependencies and package itself
$ pip install -r requirements.txt .
```

Running a Development Instance
------------------------------

``` {.sourceCode .bash}
# Bring the service up in a container.
$ docker-compose up --build
```

Running a non-dockerized Instance
------------------------------

``` {.sourceCode .bash}
# In case Docker-compose command encounters an encoding related error, you can Run the Flask app manually.
cd into app
$ export FLASK_APP=api.py
flask run
```

Running Tests
-------------

The tests themselves can be run using the tox automation tool:

``` {.sourceCode .bash}
$ tox
```

You can also select only a subset of tests to be run using the `py.test`
command. For example, to run the tests in the `tests/test_api.py`
file:

``` {.sourceCode .bash}
$ pytest tests/test_api.py
```

