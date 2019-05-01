from app import app
from flask import render_template


# @app.route('/')
# def index():
#     return 'hello'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tt')
def tt():
    name = 'Vadik'
    return render_template('index.html', n = name)