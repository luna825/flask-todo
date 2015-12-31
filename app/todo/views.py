from flask import render_template,redirect,url_for
from . import app
from ..models import Todo,TodoForm
from .. import db 

@app.route('/',methods=['POST','GET'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(content = form.todo.data)
        db.session.add(todo)
        return redirect(url_for('.index'))
    todolists = Todo.query.order_by(Todo.timestamp.desc()).all()
    return render_template('index.html',todolists=todolists,form=form)

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    return redirect(url_for('.index'))

@app.route('/done/<int:id>')
def done(id):
    todo = Todo.query.get_or_404(id)
    if todo.status:
        todo.status = False
    else:
        todo.status = True
    db.session.add(todo)
    return redirect(url_for('.index'))

@app.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
    