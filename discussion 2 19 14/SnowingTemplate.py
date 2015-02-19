import random
from Tkinter import *


root = Tk()
root.title("Snow Day!")

snowflake = PhotoImage(file="snowflake.gif")
background = PhotoImage(file="Gasson.gif")

sceneWidth = 648
sceneHeight = 432

canvas = Canvas(root, width=sceneWidth, height=sceneHeight)
canvas.grid(row=0,column=0)
canvas.create_image(sceneWidth/2, sceneHeight/2, image=background)

def updateSnow(snow, x, y):
    
    x == x
    if y < sceneHeight:
        y += 1

    canvas.coords(snow, x, y)

    canvas.after(20, updateSnow, snow, x, y)
    

def addSnow():
    x = random.randrange(0, sceneWidth+1)
    y = 0
    snow = canvas.create_image(x, y, image=snowflake)
    updateSnow(snow, x, y)

snowButton = Button(root, text="Make it snow", command=addSnow)
snowButton.grid(row=1, column=0)

root.mainloop()
