# -*- coding: utf-8 -*-

from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)

app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
cors = CORS(app)


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    contents = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, default=0, nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)
    is_done = db.Column(db.Boolean, default=False, nullable=True)

    def __init__(self, title: str, contents: str) -> None:
        self.title = title
        self.contents = contents

    def __repr__(self) -> str:
        return f'<Todo {self.title}>'


class TodoSchema(ma.ModelSchema):
    class Meta:
        model = Todo


@app.route('/todos', methods=['GET'])
def read_todos() -> list:
    todos = Todo.query.all()
    todos_schema = TodoSchema(many=True)

    result = todos_schema.dump(todos)

    return jsonify(result.data)


@app.route('/todos/<int:id>', methods=['GET'])
def read_todo(id: int) -> dict:
    todo = Todo.query.get_or_404(id)
    todo_schema = TodoSchema()

    result = todo_schema.dump(todo)

    return jsonify(result.data)


@app.route('/todos', methods=['POST'])
def create_todo() -> Response:
    todo = Todo(**request.get_json())

    print(request.get_json())

    db.session.add(todo)
    db.session.commit()

    return Response(
        '{"success": true}', status=201, mimetype='application/json')


@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id: int) -> Response:
    todo = Todo.query.get_or_404(id)

    data = request.get_json()

    todo.title = data['title']
    todo.contents = data['contents']
    todo.deadline = data['deadline']
    todo.is_done = data['is_done']
    todo.priority = data['priority']

    db.session.commit()

    return Response(
        '{"success": true}', status=200, mimetype='application/json')


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id: int) -> Response:
    todo = Todo.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return Response(
        '{"success": true}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
