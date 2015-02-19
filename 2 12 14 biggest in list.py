# Find biggest item in list, return it

# biggestSoFar = -9999999  don't want to do this
def biggest(lst):
    # global biggestSoFar
    biggestSoFar = lst[0]
    for i in lst:       # i gives the actual values of the elements in the list
        if i > biggestSoFar:
            biggestSoFar = i
    return biggestSoFar
        

a = [-7, -22, -99, -13, -649]
print "Biggest element in", a, "is", biggest(a)
