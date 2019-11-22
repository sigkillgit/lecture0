#!/usr/bin/env python
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template('index.html', new_year=new_year)

@app.route('/dynamicroute')
def bob():
    name = 'Bob'
    return render_template('bob.html', name=name)

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

if __name__ == '__main__':
    app.run(debug = True)
