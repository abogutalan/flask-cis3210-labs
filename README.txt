
LAB 3:
so we're basically letting them 'login' by checking 
if password matched what's in the db, adding a user, 
deleting a user and changing a user's password?

Abdullah Ogutalan
1109732

How it works?
- Once you run the project by following the steps below and 
you have a firefox open with the project, you will see four 
buttons e.g. GET, PUT, POST, DELETE buttons and a submit form.
All of these buttons send AJAX request to python FLASK.

GET button: gets the username and password of a default user,
then prints them in a paragraph html tag.

POST button: Submit button below is being used instead

SUBMIT button: Creates a new user by the value of email and
password inputs of sign up form. Value of email has to be any
kind of email, admin can not punch something in like "newuser"
but instead it must be like newuser@gmail.com.

PUT button: Updates the information of the user by using the
values of email and password input, so after creating a new 
user, you can change email and password input and click PUT
button above then see the updated information of the user on
the screen.

DELETE button: In order to simulate deleting information of
the user i assigned empty string to username and password
variables of the user, then print the result on the screen .

Note: There is no function of navigation bar at the top and 
Remember me check box yet.
Furthermore, you may see most of the actions on firefox console.

- Clicking my name in the footer routes to my linkedIn account,
and my student number routes to my github account.

*******************************************************************

MY NOTES:

> export FLASK_APP=app.py

Run command in the server:
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



