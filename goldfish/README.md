# Goldfish - a forgetful simple REST server

This is a server for a simple REST API. It will forget everything once the server is stopped.

## REST API

* POST `/register` : registers a new user (new user will got inside the request's body)
* POST `/login` : login with a registered user
* GET `/<user>/phrases` : return a list of phrases associated with the current user
* POST `/<user>/phrases` : adds a new pharse (passed inside the request's body)
* DELETE `/<user>/logout` : logout the current user

## Starting the server

1. Execute `virtualenv <env_name>` (if you don't have `virtualenv` run `pip install virtualenv`).
2. Execute `source ./<env_name>/bin/activate` (assuming a Linux OS).
3. Execute `pip install -r requirements.txt`.
4. Execute `python app.py`
