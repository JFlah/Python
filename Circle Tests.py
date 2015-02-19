# Tests of the Circle class

from Circle import *

c1 = Circle(Point(5,6), 4)

c2 = Circle(Point(-8,3), 6.5)

print "Circle 1:", c1
print "Circle 1 area:", c1.area() # should be 50.265...
print "Circle 1 circumference:", c1.circumference() # should be 25.132...
print
print "Circle 2:", c2
print "Circle 2 area:", c2.area() # should be 132.7
print "Circle 2 circumference:", c2.circumference() # should be 40.84
print
print "Distance from circle 1 to origin:", c1.distanceToOrigin() # should be 3.81
print "Distance from circle 2 to origin:", c2.distanceToOrigin() # should be 2.044
