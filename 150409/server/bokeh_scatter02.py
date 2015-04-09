# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 11:40:27 2015

@author: Wasit
"""
import time
import numpy as np
from six.moves import zip

from bokeh.plotting import *

def transition(sx,sy,vx,vy,m):
    dt=1
    G=0.1
    epsilon=1e0
    # http://http.developer.nvidia.com/GPUGems3/gpugems3_ch31.html
    
    for i in xrange(len(sx)):
        ax_i=0.0;
        ay_i=0.0;
        for j in xrange(len(sx)):
            if i!=j:
                rx_ij=sx[j]-sx[i]
                ry_ij=sy[j]-sy[i]
                f=(rx_ij**2 + ry_ij**2 + epsilon*2)**-1.5
                ax_i=ax_i + G*m[i]*rx_ij*f
                ay_i=ay_i + G*m[i]*ry_ij*f
            
        vx[i] = vx[i] + ax_i*dt
        vy[i]  =vy[i] + ay_i*dt
        
    sx = sx + vx*dt
    sy = sy + vy*dt
    return sx,sy,vx,vy
    
if __name__ == "__main__":
    N = 40
    
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    vx = np.zeros(shape=N)
    vy = np.zeros(shape=N)
    m=np.random.random(size=N)
    
    colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]
    
    TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
    
    #output_file("color_scatter.html", title="color_scatter.py example")
    #output_server("scatter_animate", url='http://10.200.30.55:5006/')
    output_server("scatter_animate")
    
    p = figure(tools=TOOLS)
    p.scatter(x,y, radius=m, fill_color=colors, fill_alpha=0.6, line_color=None,name="particles")
    
    show(p)  # open a browser
    #get renderer from object by tag name
    renderer = p.select(dict(name="particles"))
    #data from object
    ds = renderer[0].data_source
    while True:
        for i in xrange(len(x)):
            #update the value of the object
            #call transition function
            (x,y,vx,vy) = transition(x,y,vx,vy,m)
            ds.data["x"] = x
            ds.data["y"] = y
            cursession().store_objects(ds)
            time.sleep(0.01)