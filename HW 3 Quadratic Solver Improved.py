# John M Flaherty HW3: Quadratic Equation Solver Improved

# Get initial values A,B,C for the equation Ax^2 + Bx + C

print 'Quadratic Equations Solver'

a = float(raw_input('Enter A: ')) 

b = float(raw_input('Enter B: '))

c = float(raw_input('Enter C: '))

# For ease of use, make the discriminant a variable

disc = (b**2)-(4*a*c)
print "Disc is:", disc  # For ease of understanding the result given

# Our five cases are covered here, adjusted to avoid any overlap

if a == 0.0 and b == 0.0:
    print "There are no solutions."
    
if a == 0.0 and b != 0.0:
    print "There is one solution:", -c, "/", b
    
if disc > 0.0 and a != 0.0:
    print "There are two distinct, real solutions."
    
    root1 = (-b + ((disc))**0.5)/(2*a)

    root2 = (-b - ((disc))**0.5)/(2*a)

    print 'The solutions are', root1, 'and', root2
    
if disc == 0.0 and a != 0:
    print "There is one solution."
    root = -b/(2*a)
    print root, "is your solution."

if disc < 0.0:
    print "There are no real solutions."
