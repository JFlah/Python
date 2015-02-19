### If statement practice 1/22/14
##
### Retirement:
### An employee may retire if he or she meets at least one of these:
###   1) has worked here at least 40 yrs
###   2) is 65 or older
###   3) has worked at least 30 years and is 60 or over
##
##yearsWorked = int(raw_input("Years worked here: "))
##age = int(raw_input("Age: "))
##
### Using an IF, print either "Retire" or "Back to work"
##
##
### 'and' has higher precedence than 'or' so ( ) is not necessary
##if yearsWorked >= 40 or age >= 65 or (yearsWorked >= 30 and age >= 60):
##    print "Retire"
##else:
##    print "Back to work"
##
### General note: else's only apply to the last prior if statement



### Who won the game?
##home = int(raw_input("Home team score: "))
##opponent = int(raw_input("Enemy score: "))
##
##if home > opponent:
##    print "The home team won"
##elif home < opponent:
##    print "The away team won"
##else:                           # Only option left is for home == away
##    print "It was a tie"

# Palindromes
num = int(raw_input("Enter a 3 digit number: "))
# Is it a palindrome?
hundreds = num/100
tens = (num - hundreds*100)/10 # Subtracts the 400 from 456 for example
# num / 10 % 10 would also work for tens (/ and % have same precedence)
ones = num - hundreds*100 - tens*10 # Subtracts hundreds and tens part out
# num%10 would also give the ones digit

print "Hundreds:", hundreds
print "Tens:", tens
print "Ones:", ones

if hundreds == ones:
    print "It's a palindrome"
else:
    print "It's not a palindrome"
    
