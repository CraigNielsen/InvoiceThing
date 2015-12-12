from flask.ext.script import Manager, Server

from backend import create_app

manager = Manager(create_app)


class RunServer(Server):
    def handle(self, *args, **kwargs):
        Server.handle(self, *args, **kwargs)
manager.add_command(
    'run-server',
    RunServer(use_debugger=True, use_reloader=True),
)

if __name__ == "__main__":
    manager.run()
