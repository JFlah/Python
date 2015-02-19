power = 1

result = 3**power

while result < 1000000000:
    print result
    power = power + 1
    result = 3**power

print "power is", power
