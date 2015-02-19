# discussion 1/29/14

# Decision Maker

# Checks all same, all different, 

def all_the_same(x,y,z):
    if (x==y and y==z):
        return True
    else:
        return False

def all_different(x,y,z):
    if (x!=y and y!=z):
        return True
    else:
        return False

def max_index(x,y,z):

    lis1=[x,y,z]
    
    if (max(lis1)==x):
        return 1
    if (max(lis1)==y):
        return 2
    if (max(lis1)==z):
        return 3

print "This tells you what happened betwixt the three."

fir = int(raw_input("First score/number:"))
sec = int(raw_input("Second score/number:"))
thi = int(raw_input("Third score/number:"))

if (all_the_same(fir,sec,thi)==True):
    print "It's a three way tie!"
    
    
elif (all_different(fir,sec,thi)==True):
    print "Player/candidate", max_index(fir,sec,thi), "wins."

elif (fir==sec or sec==thi or fir==thi):
    if (fir==sec and (fir>thi and sec>thi)):
        print "It's a two way tie between the first and second!"
    if (sec==thi and (sec>fir and thi>fir)):
        print "It's a two way tie between the second and third!"
    if (fir==thi and (fir>sec and thi>sec)):
        print "It's a two way tie between the second and third!"


