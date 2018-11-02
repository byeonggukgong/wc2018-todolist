# -*- coding: utf-8 -*-

from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.extensions import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def _make_context():
    return dict(app=app, db=db)


manager.add_command('runserver', Server(host='0.0.0.0', port=8080))
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('migrate', MigrateCommand)


@manager.command
def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    manager.run()
