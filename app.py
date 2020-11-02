#!/usr/local/bin/python

from flask import Flask, render_template, request, json, session, redirect, url_for
import MySQLdb
import MySQLdb.cursors
from markupsafe import escape
import os
import hashlib

app = Flask(__name__, static_url_path='')
#app.debug = True

# Seting the secret key to some random bytes.
app.secret_key = os.urandom(16) 

db=MySQLdb.connect(
        host="dursley.socs.uoguelph.ca",
        user="aogutala",
        passwd="1109732",
        db="aogutala" )



@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        if request.method == 'POST':
            # remove the username from the session if it's there
            session.pop('username', None)
            return redirect(url_for('index')) 
    return render_template('index.html')

@app.route('/user', methods=['GET', 'PUT', 'POST', 'DELETE'])
def user():
    # getting user information
    if request.method == 'GET':
        user =  request.args['username']
        user = user.replace("."," ")
        return db_get_user(user)
    # updating user information  
    elif request.method == 'PUT':
        user =  request.form['username']
        user = user.replace("."," ")
        password = request.form['password']
        password = obscurePassword(password)
        db_update_user(user, password)
        return json.dumps({'status':'Updated user','user':user,'password':password})
    # adding a new user
    elif request.method == 'POST':
        user =  request.form['username']
        # avoiding username vulnerabilities
        user = user.replace("."," ")
        password = request.form['password']
        password = obscurePassword(password)
        db_create_user(user, password)
        session['username'] = request.form['username']
        return 'Welcome %s' % escape(session['username']) + '''
        <form method="post">
            <h3>Please click the button below to log out </h3>
            <p><input type=submit value=Logout>
        </form>
        '''
    # deleting user
    elif request.method == 'DELETE':
        user =  request.form['username']
        user = user.replace("."," ")
        db_delete_user(user)
        session.pop('username', None)
        redirect(url_for('index'))
        return json.dumps({'status':'Deleted','Deleted user':user})
    else:
        return "No request!"


# *** helper functions ***

def db_create_user(user, password):
    with db:
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS USER(\
                    Id INT PRIMARY KEY AUTO_INCREMENT, \
                    Name VARCHAR(256), Pswd VARCHAR(256))")
        # checking if the user already exists
        checkingUser = "SELECT 1 FROM USER WHERE Name=%s AND Pswd=%s"
        cur.execute(checkingUser, (user, password))
        if cur.rowcount == 1:
            return "The user already exists"
        else:  
            cmd = "INSERT INTO USER(Name,Pswd) VALUES(%s,%s)"
            cur.execute(cmd, (user, password))
            return "Created a user"

def db_update_user(user, password):
    with db:
        cur = db.cursor()
        cmd = "UPDATE USER SET Pswd=%s WHERE Name=%s"
        cur.execute(cmd, (password, user))
        return "Updated USER table"

def db_delete_user(user):
    with db:
        cur = db.cursor()
        cmd = "DELETE FROM USER WHERE Name=%s"
        cur.execute(cmd, (user,))
        return "Deleted user table"
    
def db_get_user(user):
    with db:
        cur = db.cursor()
        cmd = "SELECT Pswd FROM USER WHERE Name=%s"
        cur.execute(cmd, (user,))
        password = cur.fetchone()
    return json.dumps({'Password ':password})

def obscurePassword(password):
    salt = "5gz"
    db_password = password + salt
    h = hashlib.md5(db_password.encode())
    obscuredPswrd = h.hexdigest()
    return obscuredPswrd

