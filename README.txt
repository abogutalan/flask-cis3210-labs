
Abdullah Ogutalan
1109732  👨‍💻

LAB 9:
- After doing the steps of Lab 8 explained below,
clicking the image will show it in full screen and
the program deletes the selected image.

LAB 8:
- Once you run the program, you will see two input
boxes and show images button. Please enter a tag to
first input box to filter images, and enter an amount
to second input box to specify how many images you want
to see. Then, click the show images button and you
will see images below.

LAB 7:
- Vulnerability 1: Data tampering via path traversal
To EXPLOIT, create a new user named ..
To FIX, you should escape dangerous characters in the username 
(replacing them with safe characters) before using it. 
It was earlier suggested that we should restrict the characters 
allowed in a username, but it probably didn't occur to you 
that "." was a dangerous character. It's worth noting that 
there's a vulnerability unique to Windows servers with this 
implementation. On Windows, filenames are not case sensitive 
but Gruyere usernames are. So one user can attack another user's 
files by creating a similar username that differs only in case, 
e.g., BRIE instead of brie. So we need to not just escape unsafe 
characters but convert the username to a canonical form that is 
different for different usernames.
SOLUTION: If the username includes any "." characters, the program
replaces it with " " so that there will be no more vulnerability.

- Vulnerability 2: Information disclosure #1
To EXPLOIT, exposing the users' passwords
To FIX, Passwords should never be stored in cleartext. Instead, 
you should use password hashing. The idea is that to authenticate 
a user, you don't need to know their password, only be convinced 
that the user knows it. When the user sets their password, you store 
only a cryptographic hash of the password and a salt value. When the 
user re-enters their password later, you recompute the hash and if it 
matches you conclude the password is correct. If an attacker obtains 
the hash value, it's very difficult for them to reverse that to find 
the original password.
SOLUTION: Obscured password by generating unique hashes and salting.

- Vulnerability 3: SQL Injection
Just as XSS vulnerabilities allow attackers to inject script into web pages, 
SQL injection vulnerabilities allow attackers to inject arbitrary scripts 
into SQL queries. When a SQL query is executed it can either read or write 
data, so an attacker can use SQL injection to read your entire database as 
well as overwrite it, as described in the classic Bobby Tables XKCD comic. 
SOLUTION: Avoided building queries by string concatenation.

- Vulnerability 4: Stored XSS
To EXPLOIT, enter <a onmouseover="alert(1)" href="#">read this!</a> 
as a username and password then get password from database.
SOLUTION: Serializing the form in every Ajax calls and using
json.dump when a string value is returned. The program avoids 
prompting an alert message and shows only the returning string.

LAB 6:
- I used flickr api for this lab. Once you run the project,
you will see an input box and a SHOW IMAGE button. If you click the
button it shows random images from the Flickr. If you fill in the
input box, the program filters the images accordingly and depicts them.
The images are shown up to 4. If no images are found when searched,
the program prompts a message on the screen.

Ex input: asdasdsafda ~ img does not exist!
 

PREVIOUS LABS:

How it works? 💻 
- Once you run the project by following the steps below and 
you have a firefox open with the project, you will see four 
buttons e.g. GET, Submit, POST, DELETE buttons.
All of these buttons send AJAX request to python FLASK.

🤜  GET button: gets the password of the username from database.
You only need to punch a username in and click GET button.
then prints them in a paragraph html tag.

🤜  SUBMIT(POST) button: Creates a new user in the database by the values 
of username and password inputs of sign up form. 
Input boxes have to be filled in.
User is logged in if it is already in the database. If not, the program
creates the user account in the database and log in.
Stores the username in a session variable.

🤜 PUT button: Updates the password of the user in database, 
so after creating a new user, you can change password input of 
the user  and click PUT button above then see the updated password 
of the user on the screen.

🤜 DELETE button: Deletes the user in database by username and 
pops it out from cookies.

🤜 logout button: It pops up on the page once the user logs in or
runs the program on a new page when the user is logged in.
It clears the session when clicked.

🥊  Note: There is no function of navigation bar at the top and 
Remember me check box yet.
Furthermore, you may see most of the actions on firefox console.

- Clicking my name in the footer routes to my linkedIn account,
and my student number routes to my github account.

*******************************************************************

MY NOTES:

> export FLASK_APP=app.py

Run command in the school server:
> flask run --host=0.0.0.0 --port=19732

Run command locally:
> python -m flask run --host=0.0.0.0 --port=19732

See on the browser for school server:
> http://cis3210.socs.uoguelph.ca:19732/

See on the local browser:
> http://0.0.0.0:19732/

Seeing the processes:
> ps

Killing a process:
> kill -9 PID

jQuery library should be before bootstrap library

How to Setup and Use Bootstrap (Step-by-Step) :
https://websitesetup.org/bootstrap-tutorial-for-beginners/

AJAX - GET, POST, PUT,and DELETE:
https://dev.to/gyi2521/ajax---get-post-putand-delete--m9j

Flask : AJAX with jQuery:
https://www.bogotobogo.com/python/Flask/Python_Flask_with_AJAX_JQuery.php

RESTful Web Services using Flask:
https://medium.com/@abeeralshubat/restful-web-services-using-flask-d8b7738b12e8

How to create a simple REST API with Python and Flask:
https://medium.com/duomly-blockchain-online-courses/how-to-create-a-simple-rest-api-with-python-and-flask-in-5-minutes-94bb88f74a23

MySQL Python tutorial:
http://zetcode.com/db/mysqlpython/

Using the Python DB API, don't do this:
https://bobby-tables.com/python.html
