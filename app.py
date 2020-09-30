#!/usr/local/bin/python

from flask import Flask, render_template, request, json
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__, static_url_path='')
#app.debug = True

db=MySQLdb.connect(
        host="dursley.socs.uoguelph.ca",
        user="aogutala",
        passwd="1109732",
        db="aogutala" )


    
@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

# getting user information
@app.route('/user', methods=['GET'])
def getUser():
    user="Burhan"
    return db_get_user(user)
    # return json.dumps({'status':'Get user','user':user,'password':password})

# adding a new user
@app.route('/user', methods=['POST'])
def get_db():
    create_writers()    
    return "Connected to database"

# updating user information  
@app.route('/user', methods=['PUT'])
def updateUser():
    user =  request.form['username']
    password = request.form['password']
    db_update_user(user, password)
    return json.dumps({'status':'Updated user','user':user,'password':password})

# deleting user
@app.route('/user', methods=['DELETE'])
def deleteUser():
    user =  request.form['username']
    db_delete_user(user)
    return json.dumps({'status':'Deleted','Deleted user':user})

# adding a new user
@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    #getting data by name
    user =  request.form['username']
    password = request.form['password']
    db_create_user(user, password)
    return json.dumps({'status':'Added user','user':user,'password':password})

# *** helper functions ***

def db_create_user(user, password):
    with db:
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS USER(\
                    Id INT PRIMARY KEY AUTO_INCREMENT, \
                    Name VARCHAR(256), Pswd VARCHAR(256))")
        cmd = "INSERT INTO USER(Name,Pswd) VALUES(%s,%s)"
        cur.execute(cmd, (user, password))
        return "Created writers table"

def db_update_user(user, password):
    with db:
        cur = db.cursor()
        cmd = "UPDATE USER SET Pswd=%s WHERE Name=%s"
        cur.execute(cmd, (password, user))
        return "Created writers table"

def db_delete_user(user):
    with db:
        cur = db.cursor()
        cmd = "DELETE FROM USER WHERE Name=%s"
        cur.execute(cmd, (user,))
        return "Created writers table"
    
def db_get_user(user):
    with db:
        cur = db.cursor()
        cmd = "SELECT Pswd FROM USER WHERE Name=%s"
        cur.execute(cmd, (user,))
        password = cur.fetchone()
    return json.dumps({'Password ':password})

def create_writers():
    with db:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS Writers")
        cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                            Name VARCHAR(25))")
        cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
        cur.execute("INSERT INTO Writers(Name) VALUES('Brocan Ogutalan')")
        return "Created writers table"