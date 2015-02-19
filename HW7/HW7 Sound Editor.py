# HW 7 John M Flaherty Sound Editor

from Tkinter import *
import math
import BCAudio

root = Tk()
root.title("Music Manipulator")

def read():
    BCAudio.read(fileEntry.get())
    
def play():
    BCAudio.play()
    
def stop():
    BCAudio.stop()
    
def quiet():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    for i in range(len(left)):
        left[i] /= 2.
        right[i] /= 2.
        
def sine():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()
    
    newLeft = []
    newRight = []

    for i in range(44100*2):
        newLeft.append(math.sin((math.pi*2)*(i/44100.)*1000))
        newRight.append(math.sin((math.pi*2)*(i/44100.)*1000))
        
    left[:] = newLeft
    right[:] = newRight        
    
def maximize():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    biggestSoFarLeft = abs(left[0])
    biggestSoFarRight = abs(right[0])

    for i in range(len(left)):
        if abs(left[i]) > biggestSoFarLeft:
            biggestSoFarLeft = abs(left[i])
    for i in range(len(right)):
        if abs(right[i]) > biggestSoFarRight:
            biggestSoFarRight = abs(right[i])

    for i in range(len(left)):
        left[i] /= biggestSoFarLeft
    for i in range(len(left)):
        right[i] /= biggestSoFarRight
    
def reverse():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    newLeft = []
    newRight = []

    for i in range(len(left)-1, 0, -1):
        newLeft.append(left[i])
        newRight.append(right[i])

    left[:] = newLeft
    right[:] = newRight
    
def faster():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    newLeft = []
    newRight = []
    
    for i in range(0, len(left), 2):
        newRight.append(right[i])
        newLeft.append(left[i])

    left[:] = newLeft
    right[:] = newRight
    
def louder():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()
    maximize()

    for i in range(len(left)):
        if left[i] > 0:
            left[i] = left[i]**0.8
        else:
            left[i] = (abs(left[i])**0.8)*-1
        if right[i] > 0:
            right[i] = right[i]**0.8
        else:
            right[i] = (abs(right[i])**0.8)*-1
    
def mono():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    newMono = []

    for i in range(len(left)):
        newMono.append(((left[i]+right[i])/2))
    left[:] = newMono
    right[:] = newMono
                        

def echo():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    for i in range(5512, len(left)):
        left[i] = .25*left[i] + .75*left[i-(44100/8)]
        right[i] = .25*right[i] + .75*right[i-(44100/8)]
    
def slower():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    newLeft = []
    newRight = []

    for i in left:
        newLeft.append(i)
        newLeft.append(i)
    for i in right:
        newRight.append(i)
        newRight.append(i)

    left[:] = newLeft
    right[:] = newRight
    
def fasterNotHigher():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()
    
    newLeft = []
    newRight = []
    
    for i in range(0, len(left), 2000):
        newLeft += (left[i:i+1000])
        newRight += (right[i:i+1000])
                            
    left[:] = newLeft
    right[:] = newRight

readButton = Button(root, text="Read", command=read)
readButton.grid(row=0,column=0)

fileEntry = Entry(root)
fileEntry.grid(row=0, column=1, columnspan=2)

playButton = Button(root, text="Play", command=play)
playButton.grid(row=0, column=3)

stopButton = Button(root, text="Stop", command=stop)
stopButton.grid(row=0, column=4)

quietButton = Button(root, text="Quiet", command=quiet)
quietButton.grid(row=1, column=0)

sineButton = Button(root, text="Sine", command=sine)
sineButton.grid(row=1, column=1)

maxButton = Button(root, text="Maximize", command=maximize)
maxButton.grid(row=1, column=2)

revButton = Button(root, text="Reverse", command=reverse)
revButton.grid(row=1,column=3)

fastButton = Button(root, text="Faster", command=faster)
fastButton.grid(row=1, column=4)

louderButton = Button(root, text="Louder", command=louder)
louderButton.grid(row=2, column=0)

monoButton = Button(root, text="Mono", command=mono)
monoButton.grid(row=2, column=1)

echoButton = Button(root, text="Echo", command=echo)
echoButton.grid(row=2, column=2)

slowButton = Button(root, text="Slower", command=slower)
slowButton.grid(row=2, column=3)

fastNotHighButton = Button(root, text="Faster Not Higher",
                           command=fasterNotHigher)
fastNotHighButton.grid(row=2, column=4)

root.mainloop()
