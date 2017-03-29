#!/bin/python3
# import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(round(sum(1 for x in arr if x > 0) / n, 6))
print(round(sum(1 for x in arr if x < 0) / n, 6))
print(round(sum(1 for x in arr if x == 0) / n, 6))

