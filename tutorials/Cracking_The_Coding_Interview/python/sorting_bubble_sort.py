#!/bin/python3

n = int(input().strip())
l = [int(x) for x in input().strip().split(' ')]

j = 0
length = len(l)
numSwap = 0

for _ in range(len(l)):
    while j < (length-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            numSwap += 1
        j += 1
    length -= 1
    j = 0

print("Array is sorted in", numSwap, "swaps.")
print("First Element:", l[0])
print("Last Element:", l[-1])
