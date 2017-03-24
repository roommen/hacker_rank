n, k = map(int, input().strip().split(' '))

pair = 0
num_dict = {}

num_dict = {int(x): 1 for x in input().strip().split(' ')}

for key_val in num_dict.keys():
    if key_val + k in num_dict:
        pair += 1

print(pair)
