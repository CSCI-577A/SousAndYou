# SousAndYou

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 17.3.12.

## Development server
### Requirement: Install Angular CLI 17+ and a compatible version of node

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Starting the docker image for local testing of caching
### Requirement: download docker for desktop
`docker run --name localhost -p 6379:6379 -d redis`

## Start Backend
The backend directory contains a venv. Activate it with `source backend/venv/bin/activate`
then run `pip install -r backend\requirements.txt`

Once the requirements are loaded, run `python3 backend\flask_api.py`

If you get a ModuleNotFoundError try using 'python' instead of 'python3'.
If you receive an 'Address already in use' error and are on a Mac, you will need to turn off the AirPlay receiver while running redis. 
