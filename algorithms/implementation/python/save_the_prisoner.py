n = input().strip()

for _ in range(int(n)):
    n, m, s = map(int, input().strip().split(' '))
    print(((s - 1 + m - 1) % n) + 1)

