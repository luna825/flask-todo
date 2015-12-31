import unittest
from flask import current_app,url_for
from app import create_app,db
from app.models import Todo

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.context = self.app.app_context()
        self.context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies = True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def test_model_Todo(self):
        todo = Todo(content='flask')
        db.session.add(todo)
        db.session.commit()
        todo = Todo.query.first()
        self.assertTrue(todo.content=='flask')

    def test_index(self):
        response = self.client.get('/')
        self.assertTrue('ToDo' in response.get_data(as_text=True))

    def test_add_todo(self):
        response = self.client.post(url_for('.index'),data={
            'todo':'python'
            })
        self.assertTrue(response.status_code==302)

        response = self.client.post(url_for('.index'),data={
            'todo':'javascript'
            },follow_redirects=True)
        self.assertTrue('javascript' in response.get_data(as_text=True))

        todo1 = Todo.query.first()
        response = self.client.get(url_for('.done',id=todo1.id),
            follow_redirects=True)
        self.assertTrue('已完成' in response.get_data(as_text=True))

        response = self.client.get(url_for('.done',id=todo1.id),
            follow_redirects=True)
        self.assertTrue('未完成' in response.get_data(as_text=True))

        response = self.client.get(url_for('.delete',id=todo1.id),
            follow_redirects=True)
        self.assertFalse(todo1.content in response.get_data(as_text=True))

        response = self.client.get('/no')
        self.assertTrue('Not Found' in response.get_data(as_text=True))




