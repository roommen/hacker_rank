n = int(input())
A = [int(a) for a in input().strip().split(' ')]

unique_dict = dict()
index_ = 0
min_dist = list()

for i in A:
    index_ += 1
    if i not in unique_dict.keys():
        unique_dict[i] = index_
    else:
        value_ = unique_dict[i]
        min_dist.append(abs(index_ - value_))
        unique_dict[i] = index_

print(min(min_dist) if len(min_dist) > 0 else -1)
