# -*- coding: utf-8 -*-

from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    contents = db.Column(db.String, nullable=False)

    def __init__(self, title, contents) -> None:
        self.title = title
        self.contents = contents

    def __repr__(self) -> str:
        return f'<Todo {self.title}>'


class TodoSchema(ma.ModelSchema):
    class Meta:
        model = Todo


@app.route('/')
def index() -> str:
    return 'Hello WINTER CODING!'


@app.route('/todos', methods=['GET'])
def read_todos() -> list:
    todos = Todo.query.all()
    todos_schema = TodoSchema(many=True)

    result = todos_schema.dump(todos)

    return jsonify(result.data)


@app.route('/todos/<int:id>', methods=['GET'])
def read_todo(id: int) -> dict:
    todo = Todo.query.get(id)
    todo_schema = TodoSchema()

    result = todo_schema.dump(todo)

    return jsonify(result.data)


@app.route('/todos', methods=['POST'])
def create_todo() -> Response:
    todo = Todo(**request.get_json())

    db.session.add(todo)
    db.session.commit()

    return Response(
        '{"message": "success"}', status=201, mimetype='application/json')


@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id: int) -> Response:
    todo = Todo.query.get(id)

    todo.title = request.get_json()['title']
    todo.contents = request.get_json()['contents']

    db.session.commit()

    return Response(
        '{"message": "success"}', status=200, mimetype='application/json')


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id: int) -> Response:
    todo = Todo.query.get(id)

    db.session.delete(todo)
    db.session.commit()

    return Response(
        '{"message": "success"}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
