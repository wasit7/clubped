import time

import numpy as np

from bokeh.plotting import *

N = 80

x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)

output_server("line_animate")

p = figure()

p.line(x, y, color="#3333ee", name="sin")
p.line([0,4*np.pi], [-1, 1], color="#ee3333")

show(p)

#get renderer from object by tag name
renderer = p.select(dict(name="sin"))
#data from object
ds = renderer[0].data_source

while True:
    for i in np.hstack((np.linspace(1, -1, 100), np.linspace(-1, 1, 100))):
        #update the value of the object
        ds.data["y"] = np.sin(x * i)
        cursession().store_objects(ds)
        time.sleep(0.05)