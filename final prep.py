def removeSilence():
    left=BCAudio.getLeft()
    right=BCAudio.getRight()
    newLeft=[]
    newRight=[]
    for i in range(len(left)):
        if(left[i]!=0 or right[i]!=0):
            newLeft.append(left[i])
            newRight.append(right[i])
    left[:]=newLeft
    right[:]=newRight
