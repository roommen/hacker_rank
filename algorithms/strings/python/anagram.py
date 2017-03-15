T = int(input().strip())
for _ in range(T):
    str_ = str(input().strip())
    len_ = len(str_)
    if len_ % 2 != 0:
        print(-1)
    else:
        s1, s2 = str_[0:(len_//2)], str_[(len_//2):]

        from collections import Counter
        c1 = Counter(s1)
        c2 = Counter(s2)
        print(int(sum((c1-c2).values())))
