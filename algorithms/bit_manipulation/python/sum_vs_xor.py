n = int(input().strip())
if n == 0:
    print(1)
else:
    import math

    zero_count = str(bin(n))[2:].count('0')

    print(int(math.pow(2, zero_count)))
