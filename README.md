[![Build Status](https://travis-ci.org/cabarnes/storjmon.svg?branch=master)](https://travis-ci.org/cabarnes/storjmon)
# StorjMon - Monitor for Storj Nodes
Preliminary version with only manual updates of node information from the [Storj](https://storj.io/) API.

# Installing Dependencies
The application uses [pipenv](https://pipenv.readthedocs.io/en/latest/) for dependencies. To initialize an environment, run the following:
```sh
pipenv install
```
To install development dependencies, run the following:
```sh
pipenv install --dev
```
# Running
The application can be run using a command line interface, web interface, or in [Docker](https://www.docker.com/). The application must be run from the virtual environment created by `pipenv`. Before running any local commands, launch the `pipenv` shell by running the following:
```sh
pipenv shell
```
## Web Interface
The web interface uses [Flask](http://flask.pocoo.org/). To start the development server, run the following:
```sh
FLASK_APP=gui/monitor.py python -m flask run
```
## Command Line Interface
The command line interface can be started by running the following to see the list of options:
```sh
python -m cli
```
## Docker
The Docker image runs the web interface using [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/).

The Docker image can be built by running the following:
```sh
docker build -t storjmon .
```
The image can be started by running the following:
```sh
docker run --name storjmon -p 80:80 storjmon
```
# Testing
Testing is done using [pytest](https://docs.pytest.org/en/latest/) and [prospector](https://prospector.landscape.io/en/master/). To execute the tests, run the following:
```sh
pytest && prospector
```
**NOTE**: The development dependencies must be installed.
