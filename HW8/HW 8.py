# John M Flaherty HW 8

from Tkinter import *
import BCImage
import random

root = Tk()
root.title("BC Photoshop")

canvas = Canvas(root, width = 0,height = 0) # Width and height adjust with pic
canvas.grid(row=0, column=0, columnspan=4)

photo = None

def read():
	global photo
	photo = PhotoImage(file=imageEntry.get())
	canvas.create_image(photo.width()/2, photo.height()/2, image=photo)
	canvas.config(width=photo.width(), height=photo.height())
	
def gray():
	global photo
	pixels=BCImage.getPixels(photo)
	for row  in range(len(pixels)):
		for col in range(len(pixels[row])):
			r=pixels[row][col][0]
			g=pixels[row][col][1]
			b=pixels[row][col][2]	
			gray = r*.3 + g*.59 + b*.11
			pixels[row][col] = [gray,gray,gray]
	BCImage.setPixels(photo, pixels)

def pixelate(): 
	global photo  
	pixels=BCImage.getPixels(photo)
	for row in range(len(pixels)):
		for col in range(len(pixels[row])):
			r=pixels[row-row%10][col-col%10][0]
			g=pixels[row-row%10][col-col%10][1]
			b=pixels[row-row%10][col-col%10][2]
			pixels[row][col] = [r,g,b]
	BCImage.setPixels(photo,pixels)
	
def lighten():
	global photo
	pixels=BCImage.getPixels(photo)
	for row in range(len(pixels)):
		for col in range(len(pixels[row])):
			r=pixels[row][col][0]
			g=pixels[row][col][1]
			b=pixels[row][col][2]
			r/=255. 
			g/=255.
			b/=255.
			r=r**.8
			g=g**.8
			b=b**.8
			r*=255
			g*=255
			b*=255
			pixels[row][col] = [r,g,b]
	BCImage.setPixels(photo,pixels)

def darken():	
	global photo  
	pixels=BCImage.getPixels(photo)
	for row in range(len(pixels)):
		for col in range(len(pixels[row])):
			r=pixels[row][col][0]
			g=pixels[row][col][1]
			b=pixels[row][col][2]
			r/=255. 
			g/=255.
			b/=255.
			r=r**(1/.8)
			g=g**(1/.8)
			b=b**(1/.8)
			r*=255
			g*=255
			b*=255
			pixels[row][col] = [r,g,b]
	BCImage.setPixels(photo,pixels)
	
def saturate():
	global photo  
	pixels=BCImage.getPixels(photo)
	for row in range(len(pixels)):
		for col in range(len(pixels[row])):
			r=pixels[row][col][0]
			g=pixels[row][col][1]
			b=pixels[row][col][2]
			if r>255/2:
				r=255
			else:
				r=0
			if g>255/2:
				g=255
			else:
				g=0
			if b>255/2:
				b=255
			else:
				b=0
			pixels[row][col] = [r,g,b]
	BCImage.setPixels(photo,pixels)

def flipVertically():
	global photo  
	pixels=BCImage.getPixels (photo)
	list=[]
	for row in range(len(pixels)):
		list.append(pixels[len(pixels)-row-1])
	BCImage.setPixels(photo,list)	 

def noise():
	global photo  
	pixels=BCImage.getPixels(photo)
	for row in range(len(pixels)):
		for col in range(len(pixels[row])):
			r=pixels[row][col][0]
			g=pixels[row][col][1]
			b=pixels[row][col][2]
			r += random.randrange(-100,100)
			g += random.randrange(-100,100)
			b += random.randrange(-100,100)
			if r>255:
				r=255
			if r<0:
				r=0
			if g>255:
				g=255
			if g<0:
				g=0
			if b>255:
				b=255
			if b<0:
				b=0
			pixels[row][col] = [r,g,b]
	BCImage.setPixels(photo,pixels)

def emboss():
	global photo 
	gray()  
	pixels=BCImage.getPixels(photo)
	for row in range(len(pixels)-1):
		for col in range(len(pixels[row])-1):
			r1=pixels[row][col][0]
			g1=pixels[row][col][1]
			b1=pixels[row][col][2]
			r2=pixels[row+1][col+1][0]
			g2=pixels[row+1][col+1][1]
			b2=pixels[row+1][col+1][2]
			r = 128-(r1-r2)/2
			g = 128-(g1-g2)/2
			b = 128-(b1-b2)/2
	
			pixels[row][col] = [r,g,b]
	BCImage.setPixels(photo,pixels)	

def blur():
	global photo  
	pixels=BCImage.getPixels(photo)
	for row in range(1,len(pixels)-1):
		for col in range(1,len(pixels[row])-1):
			r=0
			g=0
			b=0
			for row2 in range(row-1,row+2): # from where you are -1 .. row 1- 1, row 1+2
				for col2 in range(col-1,col+2):
					r += pixels[row2][col2][0]
					g += pixels[row2][col2][1]
					b += pixels[row2][col2][2]
			r /= 9	
			g /= 9
			b /= 9
			pixels[row][col] = [r,g,b]
	BCImage.setPixels(photo,pixels)

def sharpen():
	global photo
	pixels=BCImage.getPixels(photo)
	blur()  
	pixels2=BCImage.getPixels(photo)
	for row in range(len(pixels)):
		for col in range(len(pixels[row])):
			r1=pixels[row][col][0]
			g1=pixels[row][col][1]
			b1=pixels[row][col][2]
			r2=pixels2[row][col][0]
			g2=pixels2[row][col][1]
			b2=pixels2[row][col][2]
			r = r1 + (r1-r2)
			g = g1 + (g1-g2)
			b = b1 + (b1-b2)
			if r>255:
				r=255
			if r<0:
				r=0
			if g>255:
				g=255
			if g<0:
				g=0
			if b>255:
				b=255
			if b<0:
				b=0
			pixels[row][col] = [r,g,b]
			
	BCImage.setPixels(photo,pixels)

imageEntry = Entry(root)
imageEntry.grid(row=1,column=0,columnspan=4, sticky = "NESW")

readButton = Button(root, text="Read", command=read)
readButton.grid(row=1, column=4, sticky = "NESW")

grayButton = Button(root, text="Gray", command=gray)
grayButton.grid(row=2, column=0, sticky = "NESW")

blurButton = Button(root, text="Blur", command=blur)
blurButton.grid(row=2, column=1, sticky = "NESW")

lightenButton = Button(root, text="Lighten", command=lighten)
lightenButton.grid(row=2, column=2, sticky = "NESW")

darkenButton = Button(root, text="Darken", command=darken)
darkenButton.grid(row=2, column=3, sticky = "NESW")

pixelateButton = Button(root, text="Pixelate", command=pixelate)
pixelateButton.grid(row=2, column=4, sticky = "NESW")

sharpenButton = Button(root, text="Sharpen", command=sharpen)
sharpenButton.grid(row=3, column=0, sticky = "NESW")

saturateButton = Button(root, text="Saturate", command=saturate)
saturateButton.grid(row=3, column=1, sticky = "NESW")

embossButton = Button(root, text="Emboss", command=emboss)
embossButton.grid(row=3, column=2, sticky = "NESW")

flipVButton = Button(root, text="Flip Vertically", command=flipVertically)
flipVButton.grid(row=3, column=3, sticky = "NESW")

noiseButton = Button(root, text="Noise", command=noise)
noiseButton.grid(row=3, column=4, sticky = "NESW")

root.mainloop()
