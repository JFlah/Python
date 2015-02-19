# 2/3/14 Text manipulation

word = "Massachusetts"

c = word[5] # "o"

print "c is", c


k = len(word)
print "length of word is", k

# set j to the last character of word
j = word[len(word)-1]

print "the last char of word is", j

z = word[2:6]  # gets index 2 through just before 6

print "Chars 2 thru 5 in your word are:", z

print word[2:]  # prints 2 through the end

print word[:4]   # prints beginning up to (not including) 4

print word.upper()  # All uppercase

up = word.upper()
print word
print up


word1 = raw_input("Enter a string: ")
word2 = raw_input("Enter a second string: ")


# can use < > >= <= == !=
# This compares one by one the alphabetical order, once it reaches two that
# are different, the one that comes first is greater
# if they are the same alphabetically all the way thru, the longer one is >
if word1 < word2:
    print word1, "is smaller"
else:
    print word1, "is greater or equal"

    

word1 = "Boston"

# for index in range(len(word1)-1 : 0 : -1): would also work
    # print word1[index],
# print

for index in range(len(word1)):
    print word1[(len(word1)-index-1)],
    # or print word1[-index-1] cuz [-1] is n, etc.  
print

# give it a string and have it return the reversed string
def rev(s):
    result = ""
    for index in range(len(s)):
        result = result + s[len(s)-index-1]
    return result

print "The reverse of:", word1, "is", rev(word1)

#recursive version

def rev2(s):
    if len(s)==1: # base case
        return s
    return rev2(s[1:]) + s[0]
print rev2(word1)

word1 = "Boston is the best city ever"

def removeSpaces(s):
    result = ""
    for index in range(len(s)):
        if s[index] == " ":
            pass                    # could just have if s[index]!=" ":
        else:                       #   result = result + s[index]
            result = result + s[index]
    return result

print removeSpaces(word1)
