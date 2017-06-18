T = int(input().strip())

for _ in range(T):
    square_nos = list()
    l, b = map(int, input().strip().split(' '))
    prod = l * b
    min_ = min(l, b)
    for n in range(1, min_+1):
        if (l % n == 0) and (b % n == 0):
            nos = prod // (n*n)
            square_nos.append(nos)

    print(min(square_nos))

