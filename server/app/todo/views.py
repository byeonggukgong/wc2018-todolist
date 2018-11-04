# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request, jsonify
from flask_cors import cross_origin

from app.extensions import db
from app.models import Todo, TodoSchema

from dateutil.parser import parse

blueprint = Blueprint('todo', __name__, url_prefix='/todos')


@blueprint.route('', methods=['GET'])
@cross_origin()
def read_todos() -> list:
    todos = Todo.query.all()
    todos_schema = TodoSchema(many=True)

    result = todos_schema.dump(todos)

    return jsonify(result.data)


@blueprint.route('/<int:id>', methods=['GET'])
@cross_origin()
def read_todo(id: int) -> dict:
    todo = Todo.query.get_or_404(id)
    todo_schema = TodoSchema()

    result = todo_schema.dump(todo)

    return jsonify(result.data)


@blueprint.route('', methods=['POST'])
@cross_origin()
def create_todo() -> Response:
    todo = Todo(**request.get_json())

    db.session.add(todo)
    db.session.commit()

    return Response(
        '{"success": true}', status=201, mimetype='application/json')


@blueprint.route('/<int:id>', methods=['PUT', 'PATCH'])
@cross_origin()
def update_todo(id: int) -> Response:
    todo = Todo.query.get_or_404(id)

    data = request.get_json()

    for key in ('title', 'contents', 'priority', 'deadline', 'is_done'):
        if key in data:
            if key == 'deadline':
                data[key] = parse(data[key])

            setattr(todo, key, data[key])

    db.session.commit()

    return Response(
        '{"success": true}', status=200, mimetype='application/json')


@blueprint.route('/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_todo(id: int) -> Response:
    todo = Todo.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return Response(
        '{"success": true}', status=200, mimetype='application/json')
