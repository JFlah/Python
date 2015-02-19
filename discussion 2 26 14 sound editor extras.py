#Discussion 2/26/14 sound editor extras


def preview():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    left[:] = left[:(44100*5)]
    right[:] = right[:(44100*5)]

##    newLeft=[]
##    newRight=[]
##
##    for i in range(0, (44100*5)):
##        newLeft.append(left[i])
##        newRight.append(right[i])
##
##    left[:] = newLeft
##    right[:] = newRight

def double():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    left = left*2
    right = right*2
    
def fade():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    for i in range(44100*5):
        left[i] *= (i/(44100*5.))
        right[i] *= (i/(44100*5.))




previewButton = Button(root, text="Preview(dsc)", command=preview)
previewButton.grid(row=3,column=1)

doubleButton = Button(root, text="Double(dsc)", command=double)
doubleButton.grid(row=3,column=2)

fadeButton = Button(root, text="Fade(dsc)",command=fade)
fadeButton.grid(row=3,column=3)
