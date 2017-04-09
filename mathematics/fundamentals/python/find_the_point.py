n = int(input().strip())
for _ in range(n):
    px, py, qx, qy = map(int, input().strip().split(' '))

    rx, ry = qx + (qx - px), qy + (qy - py)

    print(rx, ry)

