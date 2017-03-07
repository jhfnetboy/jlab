from flask import Flask
app = Flask(__name__)
from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return " <p>Your browser is %s</p>  " % user_agent


@app.route('/')
def index():
    response = make_response(<h1>This document carries a cookie.</h1>)
    response.set_cookie('answer','42')
    return response

from flask import redirect

@app.route('/')
def index():
    return redirect('http://www.example.com')
rom flask import abort

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name


Flask上下文全局变量

变量名	上下文	说明
current_app	程序上下文	当前激活程序的程序实例
g	程序上下文	处理请求时用作临时存储的对象。每次请求都会重设这个变量。
request	请求上下文	请求对象，封装了客户端发出的HTTP请求中的内容。
session	请求上下文	用户会话，用户存储请求之间需要“记住”的值的词典
程序上下文使用方法：

>>> from hello import app
>>> from flask import current_app
>>> current_app.name
Traceback(most recent call last):
...
RuntimeError:working outside of application context
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
# app.app_context()可获得一个程序上下文
=====
pippo = request.form.getlist('name[]')
pippo =  request.args.getlist('name[]')


#before_first_request：在第一个请求被处理前注册一个函数运行。
#before_request：在每一个请求前注册一个函数运行。
#after_request：如果没有未处理的异常发生，在每一个请求后注册一个函数运行。
#teardown_request：即使未处理的异常发生，在每一个请求后注册一个函数运行。
