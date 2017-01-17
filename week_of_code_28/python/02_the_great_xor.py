import math

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    ctr = 0
    for i in range(int(x)):
        if (i+1) ^ int(x) > int(x):
            ctr += 1
        i += 1
    print(ctr)
