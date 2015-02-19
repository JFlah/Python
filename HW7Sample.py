# 2/19/14 Sound HW 7

# Do everything once for left channel, once for right

import BCAudio
from Tkinter import *

def quiet():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    for i in range(len(left)):
        left[i] /= 2.
        right[i] /= 2.

def quiet():
    left = BCAudio.getLeft()
    right = BCAudio.getRight()

    newLeft = []
    newRight = []

    for s in left:
        newLeft.append(s/2.)
    for s in right:
        newRight.append(s/2.)
        
    left[:] = newLeft
    right[:] = newRight

# To go faster, you remove every other sample, make it happen more quickly
# But pitch goes higher, frequency doubles

# Louder, make the elements larger


# Go twice as fast without changing pitch:
# Take out every other wave-worth of samples

# Make it go slower, duplicate every element

# Maximize, make every element as large as possible without any of them
# exceeding [-1, 1]
Go through, find sample w largest value (furthest from zero)
multiply everything by the constant that makes that largest value + or - 1
make largest sample variable called largest (.5, mult by 2, etc.)
1/largest gives the multiplier you want for all samples.
so multiply by 1/largest.
2 Passes: once finds largest value, second multiplies all samples

# Louder after maximizing while staying within the range:
# zeros stay zero, ones stay one, all other elements:
# positive range, raise them
# negative range, lower them
nums less than 1, square root is bigger, so raise every sample to the 0.5 pow
0.8 or 0.7 alters them less, might sound less distorted.
for the negative numbers, this won't work though.
SO: for negative numbers, raise abs value of num to the power, then *= -1
but if x > 0, just do x to the pow
So use loop with if

# echo: weighted average of current and the one an eigth of a second ago
weighted average of current + 44100/8 elements ago
take array, go through, change each to weighted average of that + 44100/8 elements ago
s[i] = W * s[i] + (1-W) * s[i-(44100/8)]

FOR FIRST 1/8 of second, there is nothing to average it with
don't start at 0, start when s[i-44100/8] is > 0

if numbers ever do go outside -1, 1 --> scale it all back down


#Sine:

makes sine wave, replaces whatever music present with sine wave

1000 cycle/sec sine wave lasting for 2 seconds, same in left and right
1000 hz
arrange it so you get 2000 in 2 sec range
y = sin(kx) 0-2pi is one whole cycle


# Play and stop are BCAudio.play/.stop

# Reverse: take list from left/right channel, reverse it

# Mono:
take average of value in left and right list,  put that value into both

# Faster not higher:
no pitch change: omit pieces that sound similar instead of every other.
must pick correct time scale on which to delete
SO: copy 1000 elements to new list, skip 1000, add next 1000 to new list
