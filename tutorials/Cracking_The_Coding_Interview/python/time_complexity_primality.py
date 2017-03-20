p = int(input().strip())

import math


for _ in range(p):
    n = int(input().strip())
    divided = 0
    if n == 1:
        print('Not prime')
    elif n == 2:
        print('Prime')
    else:
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if n % i == 0:
                divided += 1
                break
        print('Not prime' if divided != 0 else 'Prime')
