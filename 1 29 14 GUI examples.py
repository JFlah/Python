# Gui Examples

from Tkinter import *

window = Tk() # window is a variable, Tk() is a fcn in Tkinter, creates window

c = 0

def do_count():
    global c # Because you pass in no arguments, it doesn't work
    c = c+1
    print c

# Not visible window yet, must make it visible

w = Label(window, text="Try the Button")
w.grid(row=0, column=0)

# Specifies which window, then adds that text to it 

# Label is something to put into a window, its a fcn, adds static text

# below, command=say_hi no () cuz not calling it, we're passing it
hi_there = Button(window, text="Count", command=do_count)
hi_there.grid(row=1, column=0)

# windows divided into columns, grid dictates which row and column
# square it will be put into


window.mainloop() # make it visible

print "This will be shown when the window closes."
print "The final value of c is:", c

# program does not proceed until mainloop() ends with window closing



          
