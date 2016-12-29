#!/bin/python3
# import sys

import string
h = [int(h_temp) for h_temp in input().strip().split(' ')]
atoz = string.ascii_lowercase

d = dict()
i = 0
while i < len(h):
    d[atoz[i]] = h[i]
    i += 1

word = input().strip()
dimension = list()

i = 0
prod = 1
while i < len(word):
    dimension.append(d.get(word[i]))
    i += 1

print(max(dimension)*len(word))
