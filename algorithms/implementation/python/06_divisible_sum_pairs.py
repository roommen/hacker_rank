#!/bin/python3
# import sys

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

# i = 0
# ctr = 0
# while i < len(a):
#     j = i + 1
#     while j < len(a):
#         if (a[i] + a[j]) % k == 0:
#             ctr += 1
#         j += 1
#     i += 1
#
# print(ctr)

res = sum((i+j) % k == 0 for x, i in enumerate(a) for j in a[x+1:])
print(res)
