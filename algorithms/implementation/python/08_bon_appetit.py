n, k = map(int, input().strip().split(' '))
c = [int(x) for x in input().strip().split(' ')]
b = int(input().strip())

print('Bon Appetit' if (sum(c) - c[k]) // 2 == b else c[k] // 2)
