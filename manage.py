import os
COV = None
if os.environ.get("FLASK_COVERAGE"):
    import coverage
    COV = coverage.coverage(branch=True,include='app/*')
    COV.start()  

from app import create_app,db
from flask.ext.script import Manager,Shell
from app.models import Todo

app = create_app('development')
manager = Manager(app)

def make_shell_context():
    return dict(db=db,Todo=Todo)
manager.add_command('shell',Shell(make_context=make_shell_context))

@manager.command
def test(cover=False):
    if cover and not os.environ.get("FLASK_COVERAGE"):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable,[sys.executable]+sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__name__))
        covdir = os.path.join(basedir,'coverage')
        COV.html_report(directory=covdir)
        print('HTML version:file://%s/index' % covdir)
        COV.erase()


if __name__ == '__main__':
    manager.run()