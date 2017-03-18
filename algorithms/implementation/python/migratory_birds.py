n = int(input())
bird_type = [int(t) for t in input().strip().split(' ')]

from collections import Counter
type_dict = Counter(bird_type)

max_key = max_val = 0
for k, v in type_dict.items():
    if v > max_val:
        max_val = v
        max_key = k

    if v == max_val:
        if k < max_key:
            max_key = k

print(max_key)
