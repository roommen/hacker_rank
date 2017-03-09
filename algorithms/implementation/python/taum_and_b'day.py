T = int(input())
for _ in range(T):
    B, W = map(int, input().strip().split(' '))
    X, Y, Z = map(int, input().strip().split(' '))

    c1 = (Y * B) + (Y * W) + (Z * B)
    c2 = (X * B) + (X * W) + (Z * W)
    c3 = (X * B) + (Y * W)
    print(min(c1, c2, c3))
