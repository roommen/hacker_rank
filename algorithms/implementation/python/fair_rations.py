N = int(input().strip())
B = [int(b) for b in input().strip().split(' ')]

if sum(B) % 2 != 0:
    print('NO')
else:
    loaves = 0
    try:
        for i in range(N):
            if B[i] % 2 != 0 and B[i+1] % 2 != 0:
                loaf = B[i]
                B[i] = loaf + 1
                loaf = B[i+1]
                B[i+1] = loaf + 1
                if sum(B) % 2 != 0:
                    print('NO')
                    break
                loaves += 2
            if B[i] % 2 != 0 and B[i+1] % 2 == 0:
                loaf = B[i]
                B[i] = loaf + 1
                loaf = B[i + 1]
                B[i+1] = loaf + 1
                if sum(B) % 2 != 0:
                    print('NO')
                    break
                loaves += 2
            if B[i] % 2 == 0 and B[i+1] % 2 != 0:
                pass
        print(loaves)
    except IndexError:
        print(loaves)
