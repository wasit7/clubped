# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 11:40:27 2015

@author: Wasit
"""
import time
import numpy as np
from six.moves import zip

from bokeh.plotting import *

N = 4000

x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]

TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"

#output_file("color_scatter.html", title="color_scatter.py example")
output_server("scatter_animate")

p = figure(tools=TOOLS)
p.scatter(x,y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None,name="particles")

show(p)  # open a browser

#get renderer from object by tag name
renderer = p.select(dict(name="particles"))
#data from object
ds = renderer[0].data_source
while True:
    for i in xrange(len(x)):
        #update the value of the object
        ds.data["y"] = y+np.random.randint(-5,5,size=len(x))
        cursession().store_objects(ds)
        time.sleep(0.01)