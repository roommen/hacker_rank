#!/bin/python3

n, t = map(int, input().strip().split(' '))
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i, j = map(int, input().strip().split(' '))
    print(min(width[i:j+1]))
