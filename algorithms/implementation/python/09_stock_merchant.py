#!/bin/python3
# import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

i = 0
ctr = 0
while i < len(c):
    print('before main pop', c)
    z = c.pop(0)
    j = 0
    print('after main pop', c)
    for x in c:
        print(x, z)
        if x == z:
            ctr += 1
            print('counter increased', ctr)
            c.pop(j)
            print('after sub pop', c)
            i = j = 0
            break
        j += 1
    i += 1

print(ctr)
