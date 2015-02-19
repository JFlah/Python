# 2/14/14 Random numbers

##import random
##
##for i in range(100):
##    print random.randrange(0, 11), # Only prints range 0 to int-1
##print
##
##
##trials = 100000

##sevens = 0.0
##twos = 0.0
##
##for i in range(trials):
##    die1 = random.randrange(1,7)
##    die2 = random.randrange(1,7) # rolls between 1 and 6 inclusive
##    total = die1 + die2
##    #print "You rolled", total
##    
##    if total == 7:
##        sevens += 1
##    if total == 2:
##        twos += 1
##
##print "The number of sevens is:", sevens, "out of", trials, "trials"
##
##print "The probability:", sevens/trials
##
##print "The number of twos is:", twos, "out of", trials, "trials"
##
##print "The probability:", twos/trials

import random

trials = 1000000
count = [0.0] * 13 # so you can have 2 through 12, your possible totals

for i in range(trials):
    die1 = random.randrange(1,7) # 1 to 6
    die2 = random.randrange(1,7)
    total = die1+die2
    count[total] += 1

for i in range(2, len(count)):
    print "Probability of rolling", i, "is", count[i] / trials

