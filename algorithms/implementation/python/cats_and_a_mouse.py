q = int(input())

for _ in range(q):
    x, y, z = map(int, input().strip().split(' '))
    A = abs(x-z)
    B = abs(y-z)
    if A < B:
        print('Cat A')
    if A > B:
        print('Cat B')
    if A == B:
        print('Mouse C')



