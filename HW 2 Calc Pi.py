# John Flaherty HW 2
# Calculation of pi

print "Approximations of pi: "

pi = 4.0

for k in range(2,501):
    firstSum = ((-1)**(k+1))/(k*2-1.)
    pi = pi + (firstSum * 4)
    print pi

print "Check out the last few values printed for your (sort of) approximate pi."
    
