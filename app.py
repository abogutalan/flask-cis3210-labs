#!/usr/local/bin/python

from flask import Flask, render_template, request, json, session, redirect, url_for
import MySQLdb
import MySQLdb.cursors
from markupsafe import escape

app = Flask(__name__, static_url_path='')
#app.debug = True

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db=MySQLdb.connect(
        host="dursley.socs.uoguelph.ca",
        user="aogutala",
        passwd="1109732",
        db="aogutala" )


    
# @app.route('/')
# def index(name=None):
#     return render_template('index.html', name=name)
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        # return 'Logged in as %s' % escape(session['username'])
        if request.method == 'POST':
            # remove the username from the session if it's there
            session.pop('username', None)
            return redirect(url_for('index')) 
        return 'Welcome %s' % escape(session['username']) + '''
        <form method="post">
            <h3>Please click the button below to log out </h3>
            <p><input type=submit value=Logout>
        </form>
        '''
    return render_template('index.html')

# getting user information
@app.route('/user', methods=['GET'])
def getUser():
    user =  request.args['username']
    return db_get_user(user)


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

# # adding a new user
# @app.route('/signUpUser', methods=['POST'])
# def signUpUser():
#     #getting data by name
#     user =  request.form['username']
#     password = request.form['password']
#     db_create_user(user, password)
#     return json.dumps({'status':'Added user','user':user,'password':password})
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #getting data by name
        user =  request.form['username']
        password = request.form['password']
        db_create_user(user, password)
        # return json.dumps({'status':'Added user','user':user,'password':password})
        session['username'] = request.form['username']
        return redirect(url_for('index', username="%s" % 'abogutalan'))
    # return '''
    #     <form method="post">
    #         <p><input type=text name=username>
    #         <p><input type=submit value=Login>
    #     </form>
    # '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

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

