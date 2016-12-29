!/bin/python3
import sys

a = [int(x) for x in input().strip().split(' ')]
b = [int(x) for x in input().strip().split(' ')]

print(sum(1 for x in range(len(a)) if a[x] > b[x]), sum(1 for x in range(len(b)) if b[x] > a[x]))

