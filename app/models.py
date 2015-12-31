from . import db
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required,Length

class Todo(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(),index=True)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.now)
    status = db.Column(db.Boolean,default=False)

class TodoForm(Form):
    todo = StringField('Add to do',validators=[Required(),Length(1,128)])
    submit = SubmitField('添加任务')