#!/bin/python3

# import sys

N = int(input().strip())

if N % 2 != 0:
    print("Weird")
elif 2 <= N <= 5:
    print("Not Weird")
elif 6 <= N <= 20:
    print("Weird")
elif N > 20:
    print("Not Weird")
