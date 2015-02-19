# Clock Demo 1/31/14

# Draw using Tkinter

# New list of Tkinter components: Button, Label, Entry, and Canvas (draw)

# Think of smallest rectangle around this oval, give upper left and lower right
# oval1 = canvas.create_oval(100,100,   400,250)

# X increases left to right, y increases from top to bottom (weird)
# Origin of a canvas is at the top left

from Tkinter import *
import time
from math import *

root = Tk()

clockHeight = 525
clockWidth = 525

minuteHandLength = clockWidth/2 * 0.9
secondHandLength = clockWidth/2
hourHandLength = clockWidth/2 * 0.4

canvas = Canvas(root, width=clockWidth, height=clockHeight)
canvas.grid(row=0, column=0)

# facePhoto = PhotoImage(file="clockface.gif")
# canvas.create_image(clockWidth/2, clockHeight/2, image=facePhoto)
#(another thing to place on Canvas)

# Think of smallest rectangle around this oval, give upper left and lower right

face = canvas.create_oval(0,0,   clockWidth,clockHeight)
minuteHand = canvas.create_line(0,0,   0,0)   # X coord left, y coord right
secondHand = canvas.create_line(0,0,   0,0)
hourHand = canvas.create_line(0,0,    0,0)

def currentSecond():
    second = int(time.time()) % 60
    return second

def currentMinute():
    minute = int(time.time()) / 60 % 60
    return minute

def currentHour():
    hour = int(time.time()) / 60 / 60 % 12 - 5 # -5 time zone correction
    return hour

def sinD(theta):
    rad = 2*pi/360. * theta
    return sin(rad)

def cosD(theta):
    rad = 2*pi/360. * theta
    return cos(rad)

def updateHands():
    second = currentSecond()
    minute = currentMinute()
    hour = currentHour() + minute/60
    minuteAngle = 90 - minute*6
    secondAngle = 90 - second*6
    hourAngle = 90 - hour*30
    # coords is a canvas object that updates coordinates
    canvas.coords(minuteHand, clockWidth/2, clockHeight/2,
                  clockWidth/2 + cosD(minuteAngle)*minuteHandLength,
                  clockHeight/2 - sinD(minuteAngle)*minuteHandLength)
    canvas.coords(secondHand, clockWidth/2, clockHeight/2,
                  clockWidth/2 + cosD(secondAngle)*secondHandLength,
                  clockHeight/2 - sinD(secondAngle)*secondHandLength)
    canvas.coords(hourHand, clockWidth/2, clockHeight/2,
                  clockWidth/2 + cosD(hourAngle)*hourHandLength,
                  clockHeight/2 - sinD(hourAngle)*hourHandLength)
    canvas.after(1000, updateHands)

updateHands()

print "Current time: ", currentHour(), ":", currentMinute(), ":", currentSecond()

root.mainloop()
