#!/bin/python3
import sys


# Complete the function below.
def StairCase(n):
    i = 1
    while i <= n:
        print(" "*(n-i) + "#"*i)
        i += 1

_n = int(input())
StairCase(_n)
