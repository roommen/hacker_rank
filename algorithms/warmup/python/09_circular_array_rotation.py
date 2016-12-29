#!/bin/python3
# import sys

n, k, q = map(int, input().strip().split(' '))
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for _ in range(k):
    a.insert(0, a[-1])
    a.pop()

for _ in range(q):
    m = int(input().strip())
    print(a[m])
