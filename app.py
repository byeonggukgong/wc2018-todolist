# -*- coding: utf-8 -*-

from flask import Flask, Response, request, jsonify

app = Flask(__name__)
app.debug = True


class Todo:
    def __init__(self, id: int, title: str, contents: str) -> None:
        self._id = id
        self._title = title
        self._contents = contents

    def to_json(self) -> dict:
        return {
            'id': self._id,
            'title': self._title,
            'contents': self._contents
        }


todos = []


@app.route('/')
def index() -> str:
    return 'Hello WINTER CODING!'


@app.route('/todos')
def get_todos() -> list:
    return jsonify(todos)


@app.route('/todo', methods=['POST'])
def create_todo() -> Response:
    todo = Todo(**request.get_json())
    todos.append(todo.to_json())

    return Response(
        '{"message": "success"}', status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
