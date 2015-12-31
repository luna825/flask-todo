from app import app,db
from flask.ext.script import Manager,Shell
from app.models import Todo

manager = Manager(app)

def make_shell_context():
    return dict(db=db,Todo=Todo)
manager.add_command('shell',Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()