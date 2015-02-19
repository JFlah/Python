# 2/10/14 draw graph of sinx

from Tkinter import *
import math

window = Tk()
window.title("Graph example")

canvasWidth = 300
canvasHeight = 300

titleLabel = Label(window, text="Graph of y=sin(x)")
titleLabel.grid(row=0, column=0)

canvas = Canvas(window, width=canvasWidth, height=canvasHeight)
canvas.grid(row=1, column=0)

prevCol = 0
prevRow = canvasHeight/2

for col in range(canvasWidth):
    x = col * 2 * math.pi / canvasWidth
    y = math.sin(x)
    row = -y * canvasHeight/2 + canvasHeight/2 # helps to exaggerate graph
    line = canvas.create_line(col, row, prevCol, prevRow) # dont need 'line ='
    prevRow = row
    prevCol = col

window.mainloop()


##for i in range(20):
##    print i,
##
##print range(20)
##
##L = range(20)
##print L
##
##for i in [6, 12, -1, 4, 24, 8]:
##    print i,
##
##for i in L:
##    print i,
##
### the range fcn just creates a list, so there are several ways to use it

##L = [12, 22, 6, 0, -1]
##print L[0]
##
##print L[1]
##
##print len(L)
##
##S = "Hello"
##print S[0]
##print S[1]
##
### Lists and strings are similar
##
##print len(L)
##print len(S)
##print L[1:3]
