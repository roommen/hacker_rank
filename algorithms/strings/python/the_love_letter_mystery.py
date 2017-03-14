T = int(input().strip())

for _ in range(T):
    str_ = str(input().strip())
    ops = 0
    for i in range(len(str_) // 2):
        ops += abs(ord(str_[i]) - ord(str_[-(i+1)]))

    print(ops)
