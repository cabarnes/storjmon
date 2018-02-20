# StorjMon - Monitor for Storj Nodes

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
The application can be run using a command line or web interface. The application must be run from the virtual environment created by `pipenv`. Before running any commands, launch the `pipenv` shell by running the following:
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
# Testing
Testing is done using [pytest](https://docs.pytest.org/en/latest/) and [prospector](https://prospector.landscape.io/en/master/). To execute the tests, run the following:
```sh
pytest && prospector
```
**NOTE**: The development dependencies must be installed.
