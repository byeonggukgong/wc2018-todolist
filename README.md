# 2018 Winter Coding Web Assignment: Todo List

## Environments

### Server

> RESTful API Server

- Platform: Ubuntu 16.04
- Language: Python 3.6.5
- Framework: Flask 1.0.2
  - Flask-SQLAlchemy 2.3.2
  - Flask-Marshmallow 0.9.0
  - Flask-CORS 3.0.6
- Database: SQLite3

```
GET /todos  # Read Todos
GET /todo/<int:id>  # Read Todo
POST /todos  # Create Todo
UPDATE /todos/<int:id>  # Update Todo
DELETE /todos/<int:id>  # Delete Todo
```

### Client

- Platform: Ubuntu 16.04
- Language: Javascript
- Runtime: Node.js v10.1.0
  - axios 0.18.0
- Framework: Vue.js 3.0.5
  - vue-datetime 1.0.0-beta.8

## Installation and Execution Methods

### Common

```
git clone https://github.com/byeonggukgong/wintercoding-todolist  # Clone into current directory
```

### Server

```
$ virtualenv --python=python3.6 .venv

$ source .venv/bin/activate  # When generated virtual environment

$ python manage.py init_db  # When acvtivated virtual environment

$ python manage.py runserver  # When activated virtual environment and database is ready
```

### Client

```
$ npm install

$ npm run serve  # When installed necessary modules
```
