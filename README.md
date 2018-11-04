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

ex) /todos 200 OK

[
    {
        "contents": "테스트를 성공적으로 완료함 :)",
        "deadline": "2018-11-03T00:00:00+00:00",
        "id": 1,
        "is_done": true,
        "priority": 3,
        "title": "실 서버 운영 테스트하기"
    },
    {
        "contents": "우여곡절 끝에 서비스 오픈함 :)",
        "deadline": null,
        "id": 2,
        "is_done": true,
        "priority": 1,
        "title": "AWS Lightsail 사용하기"
    },
    {
        "contents": "안전하게 11월 3일까지 보내기",
        "deadline": "2018-11-03T00:00:00+00:00",
        "id": 3,
        "is_done": false,
        "priority": 1,
        "title": "완료 메일 보내기"
    }
]

GET /todos/<int:id>  # Read Todo

ex) /todos/1 200 OK

{
    "contents": "테스트를 성공적으로 완료함 :)",
    "deadline": "2018-11-03T00:00:00+00:00",
    "id": 1,
    "is_done": true,
    "priority": 3,
    "title": "실 서버 운영 테스트하기"
}

POST /todos  # Create Todo

ex) /todos/1 201 OK

{
    "success": true
}

UPDATE /todos/<int:id>  # Update Todo

ex) /todos/1 200 OK

{
    "success": true
}

DELETE /todos/<int:id>  # Delete Todo

ex) /todos/1 200 OK

{
    "success": true
}
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
