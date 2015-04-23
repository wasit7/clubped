# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:48:43 2015

@author: Wasit
"""

from flask import Flask
from flask import request
app = Flask(__name__)

form_str="""<form action="login" method="POST">
First name:<br>
<input type="text" name="firstname" value="Mickey">
<br>
Last name:<br>
<input type="text" name="lastname" value="Mouse">
<br><br>
<input type="submit" value="Submit">
</form>"""

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        firstname =  request.form["firstname"]
        lastname =  request.form["lastname"]
        return "Your name is %s %s"%(firstname,lastname)
    else:
        return form_str

if __name__ == '__main__':
    app.run(debug=True)