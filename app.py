#!/usr/local/bin/python

from flask import Flask, render_template, request, json

app = Flask(__name__, static_url_path='')
#app.debug = True


@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/login', methods=['GET', 'PUT', 'POST', 'DELETE'])
def about():
    if request.method == 'GET':
        return 'GET request!!!'
    elif request.method == 'PUT':
        return 'PUT request!!!'
    elif request.method == 'POST':
        return 'POST request!!!'
    elif request.method == 'DELETE':
        return 'DELETE request!!!'
    else:
        return 'No Request!!!'

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})

    