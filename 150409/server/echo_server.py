# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 17:34:36 2015

@author: Wasit
"""
import numpy as np
from flask import Flask
from flask import Response

app=Flask(__name__)

@app.route("/")
def index():
    print "debug:index()"
    return "hello world"
    
@app.route("/echo/<text>")
def echo(text):
    print "debug:echo(%s)"%text
    return text

@app.route('/square/<number>')
def square(number):
    print "debug:square(%s)"%number
    try:
        x=float(number)
        return str(x*x)
    except ValueError:
        return "Please enter a number number"
        
@app.route('/data/')
def data():
    print "debug:data()"
    return "value\t%.3f"%np.random.rand()
    


@app.route('/data.csv')
def csv():
    def generate():
        yield "value\n%.3f"%np.random.rand()
    return Response(generate(), mimetype='text/csv')
def newdata():
    return    
if __name__ == "__main__":
    #app.run(debug=True,host='10.200.30.55')
    app.run(debug=True,host='192.168.1.33')
