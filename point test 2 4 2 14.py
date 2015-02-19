# point test 2.0 4/2/14

#draw graph of y=sin(x)

from Point import *
from Tkinter import *
import math

window = Tk()
window.title("Graph of y=sin(x)")

canvas = Canvas(window, width=360, height=360)
canvas.grid(row=0, column=0)

points=[]

def sinDegrees(angle):
    radians = angle/180.*math.pi
    s = math.sin(radians)
    return s

for x in range(360):
    y = -sinDegrees(x)*100+180 #180 shifts down, 100 stretched amplitude
    p = Point(x,y)
    points.append(p)

for p in points:
    print p
    p.plot(canvas)

window.mainloop()
