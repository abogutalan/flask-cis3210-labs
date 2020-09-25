#!/usr/local/bin/python

from flask import Flask, render_template, request, json

app = Flask(__name__, static_url_path='')
#app.debug = True


@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

# getting user information
@app.route('/user', methods=['GET'])
def getUser():
    user = 'Abdullah'
    password = 'Ogutalan'
    return json.dumps({'status':'Get user','user':user,'pass':password})

# adding a new user
@app.route('/user', methods=['POST'])
def addUser():
    return 'Submit button below is being used instead'

# updating user information  
@app.route('/user', methods=['PUT'])
def updateUser():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'Updated user','user':user,'pass':password})

# deleting user
@app.route('/user', methods=['DELETE'])
def deleteUser():
    return json.dumps({'status':'Deleted user','user':'','pass':''})

# adding a new user
@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'Added user','user':user,'pass':password})

    