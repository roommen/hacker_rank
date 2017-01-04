#!/bin/python3
# import sys

t = int(input().strip())
ctr = 0
for a0 in range(t):
    n = int(input().strip())
    for x in str(n):
        if int(x) == 0:
            pass
        else:
            if n % int(x) == 0:
                ctr += 1
    print(ctr)
    ctr = 0
