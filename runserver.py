#coding:utf-8

'''
EDPS系统运行起始程序
'''
__author__ = 'terryzhoujie'

from flask import Flask, render_template, session, flash
from flask import redirect
from flask import abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import url_for
from datetime import datetime
from form import NameForm
# from flask_script  import Manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
# manage = Manager(app)
bootstrap = Bootstrap(app)
momont = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        # name = form.name.data
        # form.name.data = ''
        oldname = session.get('name')
        if oldname is not None and oldname != form.name.data:
            flash('Look like you have changed your name')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    if name == "terry":
        url1 = url_for('static', filename='favicon.ico',  _external=True)
        url = url_for('user', name="zhoujie", _external=True)
        return redirect(url)
    return render_template('user.html', name=name, current_time = datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
