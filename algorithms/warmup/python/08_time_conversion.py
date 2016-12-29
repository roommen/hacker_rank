#!/bin/python3
# import sys

from time import strptime, strftime

time = strptime(input().strip(), '%I:%M:%S%p')
print(strftime('%H:%M:%S', time))
