# This constant time solution is taken from the discussion

l, r = int(input()), int(input())

value = l ^ r

value |= value >> 1
value |= value >> 2
value |= value >> 4
value |= value >> 8

print(value)
