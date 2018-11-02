# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request, jsonify

from app.extensions import db
from app.models import Todo, TodoSchema

from datetime import datetime

blueprint = Blueprint('todo', __name__)


@blueprint.route('/todos', methods=['GET'])
def read_todos() -> list:
    todos = Todo.query.all()
    todos_schema = TodoSchema(many=True)

    result = todos_schema.dump(todos)

    return jsonify(result.data)


@blueprint.route('/todos/<int:id>', methods=['GET'])
def read_todo(id: int) -> dict:
    todo = Todo.query.get_or_404(id)
    todo_schema = TodoSchema()

    result = todo_schema.dump(todo)

    return jsonify(result.data)


@blueprint.route('/todos', methods=['POST'])
def create_todo() -> Response:
    todo = Todo(**request.get_json())

    db.session.add(todo)
    db.session.commit()

    return Response(
        '{"success": true}', status=201, mimetype='application/json')


@blueprint.route('/todos/<int:id>', methods=['PUT', 'PATCH'])
def update_todo(id: int) -> Response:
    todo = Todo.query.get_or_404(id)

    data = request.get_json()

    for key in ('title', 'contents', 'priority', 'deadline', 'is_done'):
        if key in data:
            if key == 'deadline':
                data[key] = datetime.strptime(data[key], '%Y-%m-%dT%H:%M:%S.%fZ')
            setattr(todo, key, data[key])

    db.session.commit()

    return Response(
        '{"success": true}', status=200, mimetype='application/json')


@blueprint.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id: int) -> Response:
    todo = Todo.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return Response(
        '{"success": true}', status=200, mimetype='application/json')
