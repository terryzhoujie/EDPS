#coding:utf-8

'''
EDPS系统运行起始程序
'''
__author__ = 'terryzhoujie'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello flask</h1>"

if __name__ == '__main__':
    app.run()
