# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 17:34:36 2015

@author: Wasit
"""
import numpy as np
from flask import Flask
from flask import Response

import time  
from bokeh.plotting import *

app=Flask(__name__)
N = 80    
x = np.zeros(shape=N)
y = np.zeros(shape=N)
#bokeh server
output_server("line_animate",url='http://192.168.1.35:5006/')

p = figure()

p.line(x, y, name="myline")
p.circle(x, y, radius=0.1, size=20, name="mymarker")

show(p)

#get renderer from object by tag name
renderer = p.select(dict(name="myline"))
#data from object
ds = renderer[0].data_source
#get renderer from object by tag name
renderer2 = p.select(dict(name="mymarker"))
#data from object
ds2 = renderer2[0].data_source
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
    

@app.route('/log/<timestr>/<valuestr>')
def log(timestr,valuestr):
    print "debug:log(timestr:%s, valuestr:%s)"%(timestr,valuestr)
    global ds,x,y
    x=np.roll(x,-1)
    y=np.roll(y,-1)
    x[-1]=float(timestr)
    y[-1]=float(valuestr)
    #update the value of the object
    ds.data["x"] =x
    ds.data["y"] =y 
    ds2.data["x"] =x
    ds2.data["y"] =y 
    cursession().store_objects(ds)
    cursession().store_objects(ds2)
    time.sleep(0.05)
    return timestr+","+valuestr
    
@app.route('/data.csv')
def csv():
    def generate():
        yield "value\n%.3f"%np.random.rand()
    return Response(generate(), mimetype='text/csv')
        

    #app.run(debug=True,host='10.200.30.55')

 
if __name__=='__main__':  
    #flask server          
    app.run(debug=True,host='192.168.1.35')
    #app.run(host='192.168.1.4')
