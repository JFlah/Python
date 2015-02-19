# Final exam review
#1
def tens(n):
    if n==0:
        return 1
    return 10*tens(n-1)

print tens(3) # 1000

#2
def reverseDigits(n):
    ones = n%10
    tens = (n/10)%10
    hundreds = n/100
    return ones*100+tens*10+hundreds

#3

#4
def sum():
    mySum=0
    for n in range(1,101):
        mySum += 1/2**n
    return mySum
