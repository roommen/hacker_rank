#!/bin/python3

# import sys

n = bin(int(input()))
b = n[2:]

i = 0
j = 0
ctr = 0
unique = []
while i < len(b):
    if int(b[i]) == 1:
        ctr += 1
        i += 1
    elif int(b[i]) == 0:
        i += 1
        unique.insert(j, ctr)
        j += 1
        ctr = 0
    if i == len(b):
        j += 1
        unique.insert(j, ctr)

print(max(unique))
