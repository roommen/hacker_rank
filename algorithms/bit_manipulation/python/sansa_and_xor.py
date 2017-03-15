# The crux of the logic is:
# - if N is even the value is 0
# - if N is odd XOR the elements at positions 0, 2, 4, 6...

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    array_ = [int(num) for num in input().strip().split(' ')]
    if N % 2 == 0:
        print(0)
    else:
        if N == 2:
            print(array_[0])
        else:
            i = 0
            xor_ = array_[i] ^ array_[i + 2]
            for i in range(4, N, 2):
                xor_ ^= array_[i]
            print(xor_)
