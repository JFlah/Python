# 2/12/14 Lists

a = [3, 17, 22, 99]
print a[1]

for i in a:
    print i

for i in range(6):
    print i

print range(6) # shows list [0,1,2,3,4,5], proves range uses lists



def getSum(lst):
    total = 0.0
    for i in lst:
        total += i
        print "Adding", i, "to the total"
    return total

def getSum2(lst):
    total = 0
    for j in range(len(lst)):
        print "j is", j, "list[j] is", lst[j]
        total += lst[j]
    return total

a = [12, 13, 14, 22, -1]

x = getSum(a)
print "The sum is", x

print getSum([0,0,3,4])
print getSum([17])
print getSum( [ ] )

y = getSum2(a)
print "the sum using getSum2 is", y

a.append(33) # Adds a 33 onto the end in a new spot in the list

# Find the avg temp for the last few days
# How many of them were above avg?

n = int(raw_input("How many temperatures? "))

temps = []

for i in range(n):
    temperature = int(raw_input("Enter next temperature: "))
    temps.append(temperature)

print "You entered", temps
average = getSum(temps)/len(temps) # or n
print "The average temperature is:", average

# How many were above average?

counter = 0
for t in temps: # Can do range(len(temps)) and get a list of [0,1,2..] length
    if t > average:
        print "temperature", t, "is above average"
        counter+=1

print "The number of temperatures above average is", counter

lst = [3,4,9,22,41,-1]
print lst[1:3] # prints elements 1 up to 3 non inclusive

lst[1:3] = [444,999,888,777] # replaces elements on left with those given
print lst

str = "hello"
print str[1:3]
# str[1:3] = "world"  Doesn't work, can't do this to strings, only lists

list1 = [2,3,4]
list2 = [5,6,7]
print list1+list2  # Puts them next to one another [2....7]

str1 = "apple"
str2 = "banana"
print str1+str2 # 'applebanana'
print str1*3  #'appleappleapple'

print list1*3 # Prints the list 3 times consecutively

list1.append(99) # Adds to end of that list

del list1[1]
print list1 # removed the element at position 1
