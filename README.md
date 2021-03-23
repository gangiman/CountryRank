# CountryRank

[Slides explaining roadmap.](https://docs.google.com/presentation/d/1he0vFWSKci07okjCnfs1KLewyGTssm5IVZCtJUmSPP8/edit?usp=sharing)

Simple project that given your preferences for different country attributes returns a ranked list of countries.

The original design was:
1) `rankings` submodule that imports and pre-processes data series.
2) restrict list of countries being compared.
3) join data series into DataFrame using countries as index.
4) rank DataFrame using your preference weights.
5) return ranked list of countries.

There was a original version, but it was lost due to accidentally killed container, all that remained is this screenshot.

![List of my preferences and some links to data](image.png)


## Currently downloaded rankings

1) Social mobility by WorldBank [source](http://www.worldbank.org/en/topic/poverty/brief/what-is-the-global-database-on-intergenerational-mobility-gdim), [data](./Raw_Data/GDIMMay2018.csv)
2) IMF GDP per Capita [source](https://www.imf.org/external/datamapper/NGDPDPC@WEO/OEMDC/ADVEC/WEOWORLD), [data](./Raw_Data/imf-dm-export-20181120.csv)
3) MIPEX Immigrant Integration ranking 2015 [source](http://mipex.eu), [data](./Raw_Data/policy_indicators_finalwebsite.xlsx)
4) Human development report [source](http://hdr.undp.org/en/data), [data](./Raw_Data/2018_statistical_annex_all.xlsx)
5) Freedom of the Internet report 2018 [source](https://freedomhouse.org/sites/default/files/FOTN_2018_Final%20Booklet_11_1_2018.pdf), [data](./Raw_Data/FOTN_2018_Final_Booklet_11_1_2018_global_ranking.csv)
6) Passport Index Data [original source](https://www.passportindex.org/), [source](https://github.com/ilyankou/passport-index-dataset), [data](./Raw_Data/passport-index-country-names.csv)

## Other rankings

We are aware of the following rankings, but they have not been integrated yet:

1. Corruption Perception Index by Transparency International: [source](https://www.transparency.org/cpi)


# CountryRank API 

## Features

- **FastAPI** with Python 3.8
- **React 16** with Typescript, Redux, and react-router
- Postgres
- SqlAlchemy with Alembic for migrations
- Pytest for backend tests
- Jest for frontend tests
- Perttier/Eslint (with Airbnb style guide)
- Docker compose for easier development
- Nginx as a reverse proxy to allow backend and frontend on the same port

## Development

The only dependencies for this project should be docker and docker-compose.

### Quick Start

Starting the project with hot-reloading enabled
(the first time it will take a while):

```bash
docker-compose up -d
```

To run the alembic migrations (for the users table):

```bash
docker-compose run --rm backend alembic upgrade head
```

And navigate to http://localhost:8000

_Note: If you see an Nginx error at first with a `502: Bad Gateway` page, you may have to wait for webpack to build the development server (the nginx container builds much more quickly)._

Auto-generated docs will be at
http://localhost:8000/api/docs

### Rebuilding containers:

```
docker-compose build
```

### Restarting containers:

```
docker-compose restart
```

### Bringing containers down:

```
docker-compose down
```

### Frontend Development

Alternatively to running inside docker, it can sometimes be easier
to use npm directly for quicker reloading. To run using npm:

```
cd frontend
npm install
npm start
```

This should redirect you to http://localhost:3000

### Frontend Tests

```
cd frontend
npm install
npm test
```

## Migrations

Migrations are run using alembic. To run all migrations:

```
docker-compose run --rm backend alembic upgrade head
```

To create a new migration:

```
alembic revision -m "create users table"
```

And fill in `upgrade` and `downgrade` methods. For more information see
[Alembic's official documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script).

## Testing

There is a helper script for both frontend and backend tests:

```
./scripts/test.sh
```

### Backend Tests

```
docker-compose run backend pytest
```

any arguments to pytest can also be passed after this command

### Frontend Tests

```
docker-compose run frontend test
```

This is the same as running npm test from within the frontend directory

## Logging

```
docker-compose logs
```

Or for a specific service:

```
docker-compose logs -f name_of_service # frontend|backend|db
```

## Project Layout

```
backend
└── app
    ├── alembic
    │   └── versions # where migrations are located
    ├── api
    │   └── api_v1
    │       └── endpoints
    ├── core    # config
    ├── db      # db models
    ├── tests   # pytest
    └── main.py # entrypoint to backend

frontend
└── public
└── src
    ├── components
    │   └── Home.tsx
    ├── config
    │   └── index.tsx   # constants
    ├── __tests__
    │   └── test_home.tsx
    ├── index.tsx   # entrypoint
    └── App.tsx     # handles routing
```
