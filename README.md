# SousAndYou

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 17.3.12.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Starting the docker image for local testing of caching
## Requirement: download docker for desktop
docker run --name localhost -p 6379:6379 -d redis

## Start Backend
pip install -r backend\requirements.txt

python3 backend\flask_api.py

