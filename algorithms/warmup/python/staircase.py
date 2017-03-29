#!/bin/python3
# import sys

n = int(input().strip())

# l = 1
# for _ in range(n):
#     k = 0
#     while k < n-l:
#         print(' ', end="")
#         k += 1
#     for _ in range(l):
#         print('#', end="")
#     l += 1
#     print()
# i = 1

for i in range(1, n+1):
    print(' ' * (n-i) + '#' * i)
