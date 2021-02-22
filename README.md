# FastAPI Starter Template
Starter template for building REST APIs using FastAPI and tortoise ORM

### Features
- JWT Authentication
- Roles and Permissions
- Database migrations
- Routing
- Test Setup

### Built with
- Python FastAPI
- Tortoise ORM
- RDMS(Sqlite / MySQL / PgSQL)
- Uvicorn

### Usage
- Clone this repository
- Change .env.example.txt to .env
- Fill in the environment variables
- Run pip install -r requirements.txt to install requirements
- Run uvicorn main:app
- Happy usage

### Migrating your database
- Create your database
- Delete the initial migration file in the migration folder if any
- Define your models in the models folder provided  
- CD into project directory and run ```aerich init-db``` from your terminal to migrate initial data
- To update your db models, change the model definition and run ```aerich migrate --name <example_update>```
- Run ```aerich upgrade``` to upgrade to the latest version
- To downgrade, run ```aerich downgrade```
- To show history, run ```aerich history```
- To show heads to be migrated, run ```aerich heads```


### License
- MIT License

### Credits
- solnsumei@gmail.com