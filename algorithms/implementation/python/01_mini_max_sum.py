#!/bin/python
# import sys

nums = [int(x) for x in input().strip().split(' ')]

print(sum(nums) - max(nums), sum(nums) - min(nums))
