
Abdullah Ogutalan
1109732  👨‍💻

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
