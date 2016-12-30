#!/bin/python3
# import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    g = 1
    if n == 0:
        print(g)
    else:
        i = 0
        while i < n:
            if i == 0 or i % 2 == 0:
                g *= 2
            else:
                g += 1
            i += 1
        print(g)
