# Python has 3 way comparisons sooooo:
# If not and had to split up like java, and operand has higher precendence
# than or.

##def middle(a,b,c):
##    if b < a < c or c < a < b:
##        return a
##
##    if a < b < c or c < b < a:
##        return b
##
##    return c
##
##
##for i in range(50,1001):
##    print i, i%10

##def isPrime(a):
##    for i in range(2,a):
##        if a%i == 0:
##            return False
##    return True



    
##def greaterThanZero(lst):
##    count = 0
##    for i in lst:
##        if i>=0:
##            count += 1
##    return count
##a = [-3,-2,-1,0,1,2,3,4,5]
##print greaterThanZero(a)

def oneToTen():
    num = int(raw_input("Enter a number between 1 and 10 inclusive: "))
    if num < 1 or num > 10:
        oneToTen()
    else:
        return num
            
    
