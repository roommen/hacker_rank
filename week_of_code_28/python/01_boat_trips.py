
n, c, m = input().strip().split(' ')
n, c, m = [int(n), int(c), int(m)]
p = list(map(int, input().strip().split(' ')))

if max(p) <= c*m:
    print('Yes')
else:
    print('No')