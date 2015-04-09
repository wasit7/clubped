# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 17:24:04 2015

@author: Wasit
"""

from flask import Flask

app=Flask(__name__)

@app.route("/products/")
def products():
        return "Arduino"
        
@app.route("/contact/")
def contact():
        return "0826639266"

@app.route("/")
def index():
    print "debug:index()"
    return "hello world"
if __name__=='__main__':  
    #flask server          
    #app.run(debug=True,host='192.168.1.4')
    app.run(debug=True)