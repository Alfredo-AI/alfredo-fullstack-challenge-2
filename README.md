# Alfredo Fullstack Challenge

This challenge consists of building the necessary logic to store and retrieve a series of subscription cancellation reasons and render this information in a web-UI.

As such, it comprises the following steps:

1. load the 2 JSON files located in the `/data` and store them in a local database
2. build an endpoint to aggregate subscription cancellation reasons for all the canceled subscriptions
3. build the UI to render the received data in a graph format

## Data upload

This task consists of reading two JSON files located in the `/data` directory and upload them directly to a local database (instruction about how to setup a local database are given in the setup section).

Each JSON file name matches the table it corresponds to - there will be 2 main tables in this challenge: `subscription` (that stores information about the start and end of a subscription as well as its status, such as active, canceled, etc, and the user it belongs to) and `user` (where user info is stored). Additional information regarding the schema and how these tables are related can be found in `/backend/models` (this follows the SQLAlchemy syntax and data models which is explained in more detail [here](https://docs.sqlalchemy.org/en/14/orm/tutorial.html))

Using a [Jupyter notebook](https://jupyter.org/) with [Pandas](https://pandas.pydata.org/) can be quite useful to help you visualize the various JSON files so you can better understand how the data is structured.

You can write all the necessary logic to upload this information in the `data_upload.py` file and this script must run by calling `python data_upload.py`.

## Cancellation reasons endpoint

This endpoint receives a `GET` request and has its URL at `/cancellation_reasons` with an optional query parameter `time_window` that can have the following values: `1year`, `1month`, `1week`. This parameter (if passed) indicates the oldest cancellation reasons that should be returned, ie, if the request sent is `http://localhost:8000/cancellation_reasons?time_window=1year` then only cancellation reasons for subscriptions that ended 1 year ago or less must be returned.

This endpoint must query the database and count how many users have canceled their subscription within the specified `time_window` and group them according to their reason of cancellation.

The database queries must be done using the `async` paradigm (more details about this implementation can be found [here](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)). Moreover a boilerplate to get an `async` connection in SQLAlchemy is already implemented and can be found in `/backend/db.py`.

The endpoint must return a `List[CancellationReason]`, where the schema for each `CancellationReason` is:

```
{
    "cancellationReason": <CANCELLATION_REASON>,
    "userCount": <USER_COUNT>
}
```

The possible cancellation reasons are:
```
{
    card: "Problemas ao renovar/atualizar",
    features: "Falta de features",
    competitor: "Prefiro outras soluções disponíveis no mercado",
    price: "O preço é demasiado alto",
    value: "Não vejo valor suficiente pelo preço",
    avm: "Pouca precisão nas avaliações de imóveis",
    metasearch: "Cobertura insuficiente no metasearch",
    customization: "Poucas opções de personalização",
    team: "A equipa não utiliza a plataforma",
    closing: "Mudança de atividade/fecho de empresa",
    sold: "Não ter acesso a dados de transação",
    other: "Outra"
}
```

The existing subscription status are `active`, `canceled`, `past_due`, `pending` and `pending_expired`. Only the canceled subscriptions can have a cancellation reason.

## UI to render data

Lastly, you need to build a UI that renders the received information in a bar graph format. Besides this, the UI must have a selector to specify which `time_window` the user wants (the default value for this parameter should be `None` and, as such, whenever the UI mounts the request to get all the canceled subscriptions' reasons aggregate counts should be sent).

Whenever the user selects a different option for the `time_window` parameter a new request must be sent to get the new information.

## Main Technologies

- [FastAPI](https://fastapi.tiangolo.com/) - web framework for building APIs with Python
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and Object Relational Mapper
- [React](https://react.dev/) - JavaScript library for building user interfaces
- [Material UI](https://material-ui.com/) - React UI framework for component building and styling
- [Tremor](https://www.tremor.so/) - React components to build charts, graphs and dashboards

## Setup

The main stacks for this challenge are `python v3.10.11` and `node v18.13.0`.

To build a local Postgres database [Docker](https://www.docker.com/) technology will be used. Run the following commands to mount local database as well as a UI to see and interact with the content inside the database as you progress the challenge.

```
docker run --name alfredo-postgres -p 5432:5432 -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=thisisatest -e POSTGRES_DB=alfredo -d postgres
docker run --link alfredo-postgres:db -p 8080:8080 -d adminer
```

After running these commands you can access the newly created database at `http://localhost:8080/`. When acessing the UI, select `PostgreSQL` as the `System` and `db` as the `Server`.

After cloning the repository, go to the `/backend` directory, create and activate a [virtual environment](https://docs.python.org/3/library/venv.html) (this step is optional), and open a terminal and install the project's requirements by typing `pip install -r requirements.txt`.

To migrate the database with the necessary schema run the following commands:

```
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```

After running these commands you should have access to two newly created tables: `user` and `subscription`.

To run the app that serves the `/cancellation_reasons` endpoint go to the `/backend` folder, open a terminal and start the uvicorn server by tying `uvicorn app:app --reload`.

For the UI, the package manager used is [Yarn](https://yarnpkg.com/) and to start it go to the `/frontend` folder, open a terminal and run the following commands.

```
yarn
yarn start
```
