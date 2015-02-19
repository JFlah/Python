# Test Point class

from Point import *

a = Point(3, 2)
b = Point(-1, -1)
c = Point(0, 0)

print "The x coord of a is", a.x
print "The x coord of b is", b.x
print "The x coord of c is", c.x

print "The point a is in quadrant: ", a.getQuadrant()
print "The point b is in quadrant: ", b.getQuadrant()
print "The poitn c is in quadrant: ", c.getQuadrant()

a.move(4,4)
b.move(8,8)

print "a is now at", a.x, a.y
print "b is now at", b.x, b.y

print "point a is", a
print "point b is", b

r,t=a.polar()

print "a in polar is:", r,t
print "b in polar is:", b.polar()
