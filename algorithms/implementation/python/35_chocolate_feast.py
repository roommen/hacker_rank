n = int(input())

for _ in range(n):
    n, c, m = map(int, input().strip().split(' '))
    choc, wrappers = [int(n / c), int(n / c)]
    while wrappers >= m:
        choc += 1
        wrappers -= m
        wrappers += 1

    print(choc)
