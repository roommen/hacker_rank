n, t = map(int, input().strip().split(' '))
candy = [int(c) for c in input().strip().split(' ')]

replenish = 0
N = n
for c in candy[0:t-1]:
    remaining = n - c
    n -= c
    if n < 5:
        rep = N - remaining
        replenish += rep
        n += rep

print(replenish)
