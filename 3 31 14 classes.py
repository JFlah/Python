# Change making class
# Simulates a cash drawer with money in it, helps make change
# Make change using the coins available, even if you run out of some coins
# Ames, Spring 2014

# I'll be making TWO instance of this class later: two cash registers with different
# numbers of pennies, nickels, dimes, and quarters in each

class Change:
    def __init__(self, p=0, n=0, d=0, q=0):
        self.pennies = p
        self.nickels = n
        self.dimes = d
        self.quarters = q

    def value(self):
        return self.quarters*25 + self.dimes*10 + self.nickels*5 + self.pennies

    def makeChange(self, cents):
        quartersDesired = cents/25
        quartersGiven = min(quartersDesired, self.quarters)
        print "Quarters:", quartersGiven
        self.quarters -= quartersGiven
        cents -= quartersGiven*25

        dimesDesired = cents/10
        dimesGiven = min(dimesDesired, self.dimes)
        print "Dimes:", dimesGiven
        self.dimes -= dimesGiven
        cents -= dimesGiven*10

        nickelsDesired = cents/5
        nickelsGiven = min(nickelsDesired, self.nickels)
        print "Nickels:", nickelsGiven
        self.nickels -= nickelsGiven
        cents -= nickelsGiven*5

        penniesDesired = cents
        penniesGiven = min(penniesDesired, self.pennies)
        print "Pennies:", penniesGiven
        self.pennies -= penniesGiven
        cents -= penniesGiven

        if cents > 0:
            print "Oops ... ran out of change, still owe customer", cents, "cents"
# end of Change class



# Now some tests
register1 = Change(p=30, n=25, d=4, q=2) # calls the __init__ function
print "Register 1 total change available:", register1.value()

register2 = Change(p=9, n=6, d=2, q=7)
print "Register 2 total change available:", register2.value()

print "Change for first customer at register 1, owed 62 cents:"
register1.makeChange(62)
print

print "In register 1 now:", register1.quarters, "Quarters,", register1.dimes, "Dimes,", \
      register1.nickels, "Nickels,", register1.pennies, "Pennies"
print

print "Change for second customer at register 1, owed 30 cents:"
register1.makeChange(30)
print

print "Change for third customer at register 1, owed 52 cents:"
register1.makeChange(52)
print

print "Change for first customer at register 2, owed 52 cents:"
register2.makeChange(52)
print
