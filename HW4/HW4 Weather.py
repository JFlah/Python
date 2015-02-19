# John M Flaherty HW4: Weather

from Tkinter import *
from math import *
import bcWeather


root = Tk()
root.title('Newton Wind')

canvas = Canvas(root, width = 500, height = 500)
canvas.grid(row = 0, column = 0)
canvas.configure(background='cyan')

fiveMPHCircle = canvas.create_oval(150, 150,    350, 350)
tenMPHCircle = canvas.create_oval(50, 50,      450, 450)

arrowShaft = canvas.create_line(0,0,   0,0)
leftSide = canvas.create_line(0,0,    0,0)
rightSide = canvas.create_line(0,0,   0,0)

def sinD(theta):
    rad = 2*pi/360. * theta
    return sin(rad)

def cosD(theta):
    rad = 2*pi/360. * theta
    return cos(rad)

def updateArrow():
    windDirection = 90 - bcWeather.getWindDirection()
    r = 20 * bcWeather.getWindSpeed()

    canvas.coords(arrowShaft, 250, 250,
                  250 + (r * cosD(windDirection)),
                  250 - (r * sinD(windDirection)))
    canvas.coords(leftSide, 250 + (r * cosD(windDirection)),
                  250 - (r * sinD(windDirection)),
                  250 + ((r*0.9) * cosD(windDirection+10)),
                  250 - ((r*0.9) * sinD(windDirection+10)))
    canvas.coords(rightSide, 250 + (r * cosD(windDirection)),
                  250 - (r * sinD(windDirection)),
                  250 + ((r*0.9) * cosD(windDirection-10)),
                  250 - ((r*0.9) * sinD(windDirection-10)))
    canvas.after(1000, updateArrow)

updateArrow()

root.mainloop()
