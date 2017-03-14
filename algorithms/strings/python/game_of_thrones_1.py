str_ = str(input().strip())

str_dict = dict()

keys = 0
for s in str_:
    if s not in str_dict:
        str_dict[s] = str_.count(s)
        keys += 1

odd, even = 0, 0
for v in str_dict.values():
    if v % 2 == 0:
        even += 1
    else:
        odd += 1

if (even == keys) or (even == keys - 1):
    print('YES')
else:
    print('NO')
