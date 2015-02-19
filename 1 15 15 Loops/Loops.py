# 1/15/14 My Loop


##for i in range(1,11):
##    print "The variable i is now", i, "and the square of i is", i**2

# Goes start to (finish-1)


# Print numbers 1 through max

##max = int(raw_input("Enter the upper bound: "))
##
##for k in range(1,max+1,2):                # odd numbers only, go by 2
##    print "Now it's", k,                # comma at end keeps it all on one line
##print             # skips down to next line
##print "All done"



# Write loop that calculates 1-100 inclusive
##total = 0
##
##for i in range(1, 101):
##    total = total + i
##    #print "i is", i, "and sum is", total
##    
##print "The sum is", total


# Calculate 15!
total = 1

for i in range(1,16):
    total = total * i
print "The factorial is", total
    
