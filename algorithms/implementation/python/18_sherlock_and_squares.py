import math
n = input().strip()

for _ in range(int(n)):
    a, b = input().split(' ')
    count = (math.floor(math.sqrt(int(b))) - math.ceil(math.sqrt(int(a)))) + 1
    print(count)
