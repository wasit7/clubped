# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 11:40:27 2015

@author: Wasit
"""
import time
import numpy as np
from six.moves import zip

from bokeh.plotting import *

def transition(sx,sy,vx,vy):
    m=1.0
    dt=0.1
    G=10.0
    epsilon=1e-3
    # http://http.developer.nvidia.com/GPUGems3/gpugems3_ch31.html
    
    for i in xrange(len(sx)):
        ax_i=0.0;
        ay_i=0.0;
        for j in xrange(len(sx)):
            if i!=j:
                rx_ij=sx[j]-sx[i]
                ry_ij=sy[j]-sy[i]
                f=(rx_ij**2 + ry_ij**2 + epsilon*2)**-1.5
                ax_i=ax_i + G*m*rx_ij*f
                ay_i=ay_i + G*m*ry_ij*f
            
        vx[i] = vx[i] + ax_i*dt
        vy[i]  =vy[i] + ay_i*dt
        
    sx = sx + vx*dt
    sy = sy + vy*dt
    return sx,sy,vx,vy
    
if __name__ == "__main__":
    N = 400
    
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    vx = np.zeros(shape=N)
    vy = np.zeros(shape=N)
    
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
            #call transition function
            (x,y,vx,vy) = transition(x,y,vx,vy)
            ds.data["x"] = x
            ds.data["y"] = y
            cursession().store_objects(ds)
            time.sleep(0.01)