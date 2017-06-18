q = int(input().strip())

for _ in range(q):
    s = str(input())
    i, len_, total_, k = 0, len(s), 0, 0
    try:
        while i < len_:
            if s[i] == '1':
                j = i+1
                while s[j] == '0':
                    j += 1
                else:
                    if s[j] == '1' and s[j-1] != '1':
                        total_ += 1
                i = j
            else:
                i += 1
        print(total_)
    except IndexError:
        print(total_)
