#!/bin/python3
# import sys

n = int(input().strip())
s = input().strip()
k = int(input().strip())

dict_letter = {65: 'A', '66': 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K',
               76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V',
               87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g',
               104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q',
               114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}

# import string
cipher = str()

for x in s:
    if ord(x) in range(65, 91):
        new_ascii = ord(x) + (k % 26)
        if new_ascii in range(65, 91):
            cipher += chr(new_ascii)
        else:
            more = new_ascii - 90
            b = 64 + more
            cipher += chr(b)
    elif ord(x) in range(97, 123):
        new_ascii = ord(x) + (k % 26)
        if new_ascii in range(97, 123):
            cipher += chr(new_ascii)
        else:
            more = new_ascii - 122
            b = 96 + more
            cipher += chr(b)
    else:
        cipher += x

print(cipher)
