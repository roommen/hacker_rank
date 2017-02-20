import math

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(math.floor((N * (N-1))/2))
