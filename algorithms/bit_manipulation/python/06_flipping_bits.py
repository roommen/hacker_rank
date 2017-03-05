T = int(input().strip())

for _ in range(T):
    integer = int(input().strip())
    print((1 << 32) - (integer+1))
