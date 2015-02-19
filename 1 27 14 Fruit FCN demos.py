# Fruitful function demos

### Absolute value fcn
##
##def abs(n):
##    if n<0:
##        n = -n
##    return n
##
##for i in range(-5, 6):
##    k = abs(i)
##    print i, k





### Given a number of cents, calculate how many quags, dimes, nickels, pennies
##
##def change(cents):
##    quarters = cents/25
##    cents = cents%25
##
##    dimes = cents/10
##    cents = cents%10
##
##    nickels = cents/5
##    cents = cents%5
##
##    pennies = cents #/1 if you're OCD
##
##    return quarters, dimes, nickels, pennies
##
##q, d, n, p = change(8) # Assigns by position, so returned quarters goes to q
##print "Change for 8 cents is:"
##if q>0:
## print "Quarters:", q
##if d>0:
##    print "Dimes:", d
##if n>0:
##    print "nickels:", n
##if p>0:
##    print "pennies:", p





# Recursive function demos


##def countdown(n):
##    if n==0:                   # Base case
##        print "Blast Off!"
##    else:
##        print n                    
##        countdown(n-1)         # Argument works towards base case
##
##countdown(20)


# Precondition: n must be >= 0

##def factorial(n):
##    if n<=0:
##        return 1
##    return n * factorial(n-1)
##for i in range(0,31):
##    print i, "! =", factorial(i)



# Fibonacci sequence index
# Takes argument of index, gives the value of the sequence at that index

def fib(i):
    if i<=1:
        return 1
    return fib(i-1) + fib(i-2)  # Returns sum of two numbers before it

print "fib(8) is", fib(8)
