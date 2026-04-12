# General project notes
This simple clinic app has a front end and a backend. The backend must be running so that data options are populated in the front end. Run locally.

## Setup
To get a list of ICN10 codes, a web scaping file has been set up.
This repository already includes a JSON of codes to seed the database. In the event you want to collect more codes, check the `scrape.py` file and increase the number of target codes you want to obtain.

To scrape and get more codes:
```
$ python scrape.py
```


## Frontend
Install packages to set up front end, then run dev script.
```
$ cd frontend
$ npm install
$ npm run dev
```

Project will run on localhost:3000. A proxy connection is set up in Nuxt so that the backend can be contacted without triggering CORS issues, or other authorization issues.


## Backend
Create and activate virtual environment.
Example:
```
$ source .venv/bin/activate
```

Install packages, and then run backend.
```
$ cd api
$ pip install -r "requirements.txt"
$ fastapi dev 
```

API will run on localhost:8000

See the [Swagger documentation](localhost:8000/docs)

The database will automatically get seeded with code data from `code_dump.json` when the user first tries to get a list of diagnosis codes.