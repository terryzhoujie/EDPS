#coding:utf-8

'''
EDPS系统运行起始程序
'''
__author__ = 'terryzhoujie'

from flask import Flask, render_template
from flask import redirect
from flask import abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import url_for
from datetime import datetime
# from flask_script  import Manager

app = Flask(__name__)
# manage = Manager(app)
bootstrap = Bootstrap(app)
momont = Moment(app)

@app.route('/')
def index():
    # return "<h1>hello flask</h1>"
    return render_template('index.html')

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
