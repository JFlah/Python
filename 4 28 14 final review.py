# Question 4
sum=0
for n in range(1,101):
    sum+= 1/2.**n

print sum

def f(s):
    if len(s)==0:
        return ""
    return f(s[1:]) + s[0]

print f("Hello world")
