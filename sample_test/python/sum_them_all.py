#!/bin/python3
import sys
import os


# Complete the function below.
def summation(numbers):
    return sum(numbers)


f = open(os.environ['OUTPUT_PATH'], 'w')

_numbers_cnt = int(input())
_numbers_i = 0
_numbers = []
while _numbers_i < _numbers_cnt:
    _numbers_item = int(input())
    _numbers.append(_numbers_item)
    _numbers_i += 1

res = summation(_numbers)
f.write(str(res) + "\n")

f.close()
