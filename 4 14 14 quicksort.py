# 4 14 14
# quicksort

data = [2, 3, 15, 1, 12, 7, 6, 14, 12, 98, 99, 7]

def partition(lst, left, right):
    while True:
        while left < right and lst[left] < lst[right]:
            right = right - 1
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left = left + 1
        else:
            return left
        while left < left and lst[left] < lst[right]:
            left = left + 1
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
            right = right - 1
        else:
            return right

def quicksort(lst, left, right):
    if left >= right:
        return
    pivot = partition(lst, left, right)
    quicksort(lst, left, pivot - 1)
    quicksort(lst, pivot + 1, right)

quicksort(data, 0, len(data) - 1)
print "After sorting:", data
