#!/bin/python
# import sys

n = int(input().strip())
c = [int(x) for x in input().strip().split(' ')]

tot = 0
d = {}
for i in range(n):
    if c[i] in d:
        d.pop(c[i])
        tot += 1
    else:
        d[c[i]] = 1

print(tot)
