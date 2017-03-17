n = input().strip()
import math
share = 0

for x in range(1, int(n)+1):
    if x == 1:
        share = math.floor(5/2)
        receive2 = share * 3
    else:
        receive = receive2
        share += math.floor(receive/2)
        receive2 = math.floor(receive/2) * 3

print(share)


