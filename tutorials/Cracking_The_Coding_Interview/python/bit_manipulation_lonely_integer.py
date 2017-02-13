n = int(input().strip())
A = [int(x) for x in input().strip().split(' ')]

unique_hashmap = dict()

for num in A:
    if num in unique_hasmap:
        value = unique_hasmap[num]
        unique_hashmap[num] = value + 1
    else:
        unique_hashmap[num] = 1

for key, value in unique_hashmap.items():
    if value == 1:
        print(key)
        break
