
## Setup

The first thing to do is to clone the repository:
``` bash
$ git clone https://github.com/Hassan-Ahmadi/sos.git
$ cd sos
```

Create a virtual environment to install dependencies in and activate it:
``` bash
$ virtualenv --no-site-packages .venv
$ source .venv/bin/activate
```

Then install the dependencies:

``` bash
(venv)$ pip install -r requirements.txt
```

Once pip has finished downloading the dependencies:
``` bash
# For the first time run
(venv)$ python manage.py migrate

# create a super user
(venv)$ python manage.py createsuperuser
```

## Run

To run the project after completing the setup:

``` bash
(venv)$ python manage.py runserver

```

## Documentation

Documents are located in `docs` directory. Also you can run the following command to serve them via `mkdocs` for easier access:

``` bash
(venv)$ mkdocs serve -a 127.0.0.1:8001
```

## Tests

To run the tests for the view simply run:
``` bash
(venv)$ python manage.py test apps.insurances.tests.test_views
```