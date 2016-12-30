#!/bin/python3
# import sys

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

a_divisible = list()
final = list()

for x in range(min(a), max(b)+1):
    ctr = 0
    for y in a:
        if x % y == 0:
            ctr += 1
    if ctr == len(a):
        a_divisible.append(x)

for x in a_divisible:
    ctr = 0
    for y in b:
        if y % x == 0:
            ctr += 1
    if ctr == len(b):
        final.append(x)

print(len(final))
