# Bubble Sort

import random
import time
import sys
from QuickSort import *

def verify(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            print "sort failed"
            return

def bubbleSort(lst):
    changed = False
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            changed = True
    if not changed: # same as if changed == False
        return
    else:
        bubbleSort(lst)

print "Original maximum recursion depth:", sys.getrecursionlimit()
sys.setrecursionlimit(11000)
print "Recursion limit is now", sys.getrecursionlimit()

print "size, bubble sort time, quick sort time"
for size in [10,100,1000,2000,3000,4000,5000,6000,7000,8000,10000]:
    # fill list with random number
    list1=[]
    for i in range(size):
        list1.append(random.random())

    # measure bubblesort time
    start = time.time()
    bubbleSort(list1)
    end = time.time()
    sortTime = end-start

    # measure quicksort time
    start = time.time()
    quicksort(list2, 0, len(list2)-1)
    end = time.time()
    quicksortTime = end-start
    #print "List size:", size, "time to sort:", sortTime
    print size, ",", sortTime, ",", quicksortTime

