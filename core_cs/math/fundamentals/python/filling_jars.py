N, M = map(int, input().strip().split(' '))

sum_total = 0

for _ in range(M):
    a, b, k = map(int, input().strip().split(' '))
    sum_total += (b - a + 1) * k

import math

print(math.floor(sum_total/N))
