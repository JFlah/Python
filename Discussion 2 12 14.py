##power = 1
##
##result = 3**power
##
##while result < 1000000000:
##    print result
##    power = power + 1
##    result = 3**power
##
##print "power is", power

#FCNS:
#ord() takes a char and returns the number value
#chr() takes a number and converts to char

def translate_char(c):
    if c in 'adgjmptw':
        return c + ' '
    if c in 'behknqux':
        return chr(ord(c)-1)*2 + ' '
    if c in 'cfilorvy':
        return chr(ord(c)-2)*3 + ' '
    if c in 'sz':
        return chr(ord(c)-3)*4 + ' '
    if c == ' ':
        return '  '
    return c

def flip_phone_text(s):
    message = ''
    s=s.lower()
    for c in s:
        message+= translate_char(c)
    return message
