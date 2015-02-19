# John Flaherty HW 2
# Calculation of "e"

import math

print "Approximations of e: "

e = 0

for k in range(0,26):
    firstSum = float((k+1))/(math.factorial(k))
    e = e + (firstSum/2)
    print e

print "Check out the last few values printed for your approximate value of e."
