#!/bin/python3
# import sys
import re

firstName = list()
emailID = list()
alph_firstName = list()

N = int(input().strip())
for _ in range(N):
    fname, email = input().strip().split(' ')
    firstName.append(fname)
    emailID.append(email)

i = 0
while i < int(N):
    if re.match('.+@gmail\.com$', emailID[i]) is not None:
        alph_firstName.append(firstName[i])
    i += 1

for sort_fname in sorted(alph_firstName):
    print(sort_fname)
