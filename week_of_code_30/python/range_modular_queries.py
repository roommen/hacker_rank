n, q = map(int, input().strip().split(' '))

A = [int(a) for a in input().strip().split(' ')]

for _ in range(q):
    left, right, x, y = map(int, input().strip().split(' '))
    criteria = 0
    for i in range(left, right+1):
        if A[i] % x == y:
            criteria += 1

    print(criteria)
