from flask import current_app
from flask.ext.script import Manager, Server, Command, Shell
from backend import create_app, db
from backend import models

manager = Manager(
    create_app,
    with_default_commands=False,
)


class RunServer(Server):
    def handle(self, *args, **kwargs):
        Server.handle(self, *args, **kwargs)
manager.add_command(
    'run-server',
    RunServer(use_debugger=True, use_reloader=True))


class CreateAll(Command):
    def run(self):
        db.create_all()
manager.add_command('create-all', CreateAll())


class DropAll(Command):
    def run(self):
        db.drop_all()
manager.add_command('drop-all', DropAll())


class InitDB(Command):
    def run(self):
        db.drop_all()
        db.create_all()
manager.add_command('init-db', InitDB())


def _make_context():
    context = dict(
        db=db,
        current_app=current_app,
    )
    context.update(vars(models))
    return context
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()
