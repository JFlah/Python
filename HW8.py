# John M Flaherty HW 8

from Tkinter import *
import BCImage
import random

root = Tk()
root.title("BC Photoshop")

canvas = Canvas(root,width = 0,height = 0) # Width and height adjust with pic
canvas.grid(row=0, column=0, columnspan=4)

photo = None 

def read():
    global photo
    photo = PhotoImage(file=imageEntry.get())
    canvas.create_image(photo.width()/2, photo.height()/2, image=photo)
    canvas.config(width= photo.width(), height=photo.height())

def gray():
    global photo
    pixels = BCImage.getPixels(photo)
    for row in range(len(pixels)):
        for col in range(len(pixels[row])):
            r = pixels[row][col][0]
            g = pixels[row][col][1]
            b = pixels[row][col][2]

            gray = (r*.3+g*.59+b*.11)

            pixels[row][col] = [gray,gray,gray]

    BCImage.setPixels(photo, pixels)

def blur():
    pass

def lighten():
    pass

def darken():
    pass

def pixelate():
    pass

def sharpen():
    pass

def saturate():
    pass

def emboss():
    pass

def flipVertically():
    pass

def noise():
    pass

imageEntry = Entry(root)
imageEntry.grid(row=1,column=0,columnspan=4)

readButton = Button(root, text="Read", command=read)
readButton.grid(row=1, column=4)

grayButton = Button(root, text="Gray", command=gray)
grayButton.grid(row=2, column=0)

blurButton = Button(root, text="Blur", command=blur)
blurButton.grid(row=2, column=1)

lightenButton = Button(root, text="Lighten", command=lighten)
lightenButton.grid(row=2, column=2)

darkenButton = Button(root, text="Darken", command=darken)
darkenButton.grid(row=2, column=3)

pixelateButton = Button(root, text="Pixelate", command=pixelate)
pixelateButton.grid(row=2, column=4)

sharpenButton = Button(root, text="Sharpen", command=sharpen)
sharpenButton.grid(row=3, column=0)

saturateButton = Button(root, text="Saturate", command=saturate)
saturateButton.grid(row=3, column=1)

embossButton = Button(root, text="Emboss", command=emboss)
embossButton.grid(row=3, column=2)

flipVButton = Button(root, text="Flip Vertically", command=flipVertically)
flipVButton.grid(row=3, column=3)

noiseButton = Button(root, text="Noise", command=noise)
noiseButton.grid(row=3, column=4)

root.mainloop()
