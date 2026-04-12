# General project notes
This simple clinic app has a front end and a backend. The backend must be running so that data options are populated in the front end. Run locally.

# Frontend
```
$ cd frontend
$ npm install
$ npm run dev
```

Project will run on localhost:3000

# Backend
```
$ cd api
$ pip install -r "requirements.txt"
$ fastapi dev 
```

API will run on localhost:8000

See the Swagger documentation at localhost:8000/docs

The database will automatically get seeded with data from `code_dump.json` when it first runs to populate a list of ICN10 diagnosis codes.
