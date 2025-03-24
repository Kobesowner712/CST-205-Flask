from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/hello')
def hello():
    print('is this thing on?')
    return '<h1>Hello world from Flask!</h1>'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2

@app.route('/myfirsttemplate')
def t1():
    print('is this thing on?')
    return render_template('my_template_1.html')