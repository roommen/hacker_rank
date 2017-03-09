p, q = map(int, (input().strip(), input().strip()))
kaprekar = list()

for k in range(p, q+1):
    square_ = k * k
    if k not in [10, 100, 1000, 10000, 100000]:
        left = str(square_)[:len(str(square_))//2]
        right = str(square_)[len(str(square_))//2:]
        if left == "":
            left = 0
        if right == "":
            right = 0
        if (int(left) + int(right)) == k:
            kaprekar.append(k)

if len(kaprekar) > 0:
    print(*kaprekar)
else:
    print('INVALID RANGE')
