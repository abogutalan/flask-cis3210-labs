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
    user = 'Abdullah'
    password = 'Ogutalan'
    return json.dumps({'status':'Get user','user':user,'pass':password})

# adding a new user
@app.route('/user', methods=['POST'])
def get_db():
    create_writers()    
    return "Connected to database"

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

    