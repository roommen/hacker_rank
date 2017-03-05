n, k = map(int, input().strip().split(' '))
height_array = [int(h) for h in input().strip().split(' ') if int(h) > k]

magic_beverage = 0

for h in sorted(height_array):
    if h > k:
        magic_beverage += (h - k)
        k = h

print(magic_beverage)
