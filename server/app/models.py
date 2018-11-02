# -*- coding: utf-8 -*-

from app.extensions import db, ma


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
