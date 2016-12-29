#!/bin/python3
# import sys

n = int(input().strip())
a = list()
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diag1 = 0
diag2 = 0
k = 1
for i in range(n):
    diag1 += a[i][i]
    diag2 += a[i][0-k]
    i += 1
    k += 1

print(abs(diag1 - diag2))
