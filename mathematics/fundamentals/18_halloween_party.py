#!/bin/python3

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    q = k//2
    print(q*q if k % 2 == 0 else q*(q+1))

