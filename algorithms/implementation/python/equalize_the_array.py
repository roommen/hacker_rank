n = int(input().strip())
array_ = [int(x) for x in input().strip().split(' ')]

dict_array = dict()
max_val = 0
max_count = 0

for a in array_:
    if a not in dict_array:
        dict_array[a] = array_.count(a)
        if array_.count(a) > max_count:
            max_count = array_.count(a)
            max_val = a

ops = 0
for k, v in dict_array.items():
    if k != max_val:
        ops += v

print(ops)
