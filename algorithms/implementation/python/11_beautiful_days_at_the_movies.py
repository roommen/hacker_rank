i, j, k = map(int, input().strip().split(' '))

ctr = 0

for x in range(i, j+1):
    if abs(x - int(str(x)[::-1])) % k == 0:
        ctr += 1

print(ctr)
