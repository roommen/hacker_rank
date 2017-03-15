n = int(input().strip())
A = [int(a) for a in input().strip().split(' ')]

m = int(input().strip())
B = [int(b) for b in input().strip().split(' ')]

from collections import Counter

dict_a = Counter(A)
dict_b = Counter(B)

lost_nums = list()
for k, v in dict_b.items():
    if k not in dict_a:
        lost_nums.append(k)
    else:
        v1 = dict_a[k]
        if v > v1:
            lost_nums.append(k)

print(*sorted(lost_nums))
