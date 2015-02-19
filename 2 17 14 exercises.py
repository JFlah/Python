# 2/17/14

# take list, double each indice

def double(lst):
    result = []
    for i in lst:
        result += [i*2]
    return result

def double2(lst):
    for i in range(len(lst)):
        lst[i] = lst[i]*2

a=[8,4,3,1,-6,13]
print "list before doubling:", a
a = double(a)
print "list after doubling:", a



def reverse(lst):
    lst2 = []
    for i in range(len(lst)-1, -1, -1):
        lst2.append(lst[i])
    return lst2
        
a = [8,4,3,1,-6,13]

b = reverse(a)

print "Original:", a
print "Reversed:", b


def reverse2(lst):
    newList=[]
    for i in lst:
        newList.insert(0, i)
    return newList

print reverse2([8,4,3,1,-6,13])


# del every 2nd element starting with the first

def delEverySecondElement(lst):
    for i in range(0, len(lst)/2):
        del lst[i]
    

a = [8,4,3,1,-6,13,20,999]

print delEverySecondElement(a)
    
