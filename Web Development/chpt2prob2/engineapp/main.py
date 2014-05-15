#!/usr/bin/env python
#Blog signup
import webapp2
import re

form = """
<form method="post">
	<h1>Signup</h1>
	<br>
	<pre>Username:         <input type = "text" name = "username" value = %(username)s> <b style="color:red">%(usr_err)s</b>
	<pre>Password:         <input type = "password" name = "password" value = %(password)s> <b style="color:red">%(pass_err)s</b>
	<pre>Retype Password:  <input type = "password" name = "verify" value = %(verify)s> <b style="color:red">%(ver_err)s</b>
	<pre>Email (optional): <input type = "text" name = "email" value = %(email)s> <b style="color:red">%(eml_err)s</b>
	<pre> <input type = "submit">
</form>
"""

welcome_form = """
<form method="get">
    <h1>Welcome %(username)s!</h1>
</form>
"""

class BaseHandler(webapp2.RequestHandler):

    def write_form(self, username="", password="", verify="",
         email="", usr_err="", pass_err="", ver_err="", eml_err=""):
            self.response.out.write(form % {"username": username,
                                            "password": password,
                                            "verify": verify,
                                            "email": email,
                                            "usr_err": usr_err,
                                            "pass_err": pass_err,
                                            "ver_err": ver_err,
                                            "eml_err": eml_err})

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        name_fail = valid_usr(username)
        pass_fail = valid_pass(password)
        ver_fail = (password!=verify)
        email_fail = valid_email(email)

        error = (name_fail or pass_fail or ver_fail or email_fail)

        if error:
            name_err=""
            pass_err=""
            ver_err=""
            email_err=""

            if name_fail:
                name_err = "Invalid Username!"
            if pass_fail:
                pass_err = "Invalid Password!"
            if ver_fail:
                ver_err = "Passwords Don't Match!"
            if not email_fail:
                email_err = "Invalid Email!"
            self.write_form( username, "", "", email, name_err, pass_err, ver_err, email_err)
        else:
        	self.write_form( username, password, password, email, "Success", "Success", "Success", "Success")

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_usr(username):
    return not(username and USER_RE.match(username))

PASS_RE = re.compile(r"^.{3,20}$")
def valid_pass(password):
    return not(password and PASS_RE.match(password))

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class WelcomeHandler(webapp2.RequestHandler):

    def get(self):
    	username = self.request.get("username")
        self.response.out.write(welcome_form % {"username": username})

app = webapp2.WSGIApplication([
    ('/', BaseHandler), ('/welcome', WelcomeHandler)], debug=True)

