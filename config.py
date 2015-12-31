import os

basedir = os.path.abspath(os.path.dirname(__name__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'todo-data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
SECRET_KEY = 'hard to guess'