#!/bin/python3
# import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

i = 0
numSwaps = 0
while i < n:
    j = 0
    while j < n-1:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
        j += 1
    if numSwaps == 0:
        break
    i += 1

print("Array is sorted in", numSwaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
