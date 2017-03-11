n, k = map(int, input().strip().split(' '))
clouds = [int(c) for c in input().strip().split(' ')]

E = 100
i = 0
while E > 0:
    if clouds[i] == 1:
        E -= 2
    E -= 1
    i = (i+k) % n

    if i == 0:
        print(E)
        break
