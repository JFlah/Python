# John Flaherty HW6

from Tkinter import *
import random

tankWidth = 500
tankHeight = 400

root = Tk()
root.title("Fish Tank")

tank = Canvas(root, width=tankWidth, height=tankHeight)
tank.grid(row=0, column=0)

fishLeft = PhotoImage(file="fishLeft.gif")

fishRight = PhotoImage(file="fishRight.gif")

tankPhoto = PhotoImage(file="tank.gif")
tank.create_image(tankWidth/2, tankHeight/2, image=tankPhoto)

def updateFish(xCoord, yCoord, dxCoord, dyCoord, image):

    if xCoord < 0 or xCoord > tankWidth:
        dxCoord *= -1
    if yCoord < 0 or yCoord > tankHeight:
        dyCoord *= -1
        
    xCoord += dxCoord
    yCoord += dyCoord
    tank.coords(image, xCoord, yCoord)

    if dxCoord < 0:
        tank.itemconfig(image,image=fishLeft)
    else:
        tank.itemconfig(image,image=fishRight)

    tank.after(20, updateFish, xCoord, yCoord, dxCoord, dyCoord, image)

def createFish():
    x = random.randrange(0, tankWidth+1)
    y = random.randrange(0, tankHeight+1)
    dx = random.randrange(-3, 4)
    dy = random.randrange(-3, 4)
    image = tank.create_image(x, y, image=fishRight)
    updateFish(x, y, dx, dy, image)

fishButton = Button(root, text="Add New Fish", command=createFish)
fishButton.grid(row=1, column=0)

root.mainloop()

