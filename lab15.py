from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return '<h1>Hello world from Flask!</h1> <p>Genevieve M. : afaik</p> ' '<p>McDonald, D. : idk</p>'

@app.route('/douglas')
def acronym():
    return render_template('template.html')