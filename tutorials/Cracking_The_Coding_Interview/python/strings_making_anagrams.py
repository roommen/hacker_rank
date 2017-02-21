a = str(input().strip())
b = str(input().strip())

dict_a = {}
dict_b = {}

for alphabet in a:
    if alphabet in dict_a:
        val = dict_a[alphabet]
        dict_a[alphabet] = val + 1
    else:
        dict_a[alphabet] = 1

for alphabet in b:
    if alphabet in dict_b:
        val = dict_b[alphabet]
        dict_b[alphabet] = val + 1
    else:
        dict_b[alphabet] = 1

ctr = 0

for k, v in dict_a.items():
    if k not in dict_b:
        ctr += dict_a[k]
    else:
        if v > dict_b[k]:
            ctr += (v - dict_b[k])
        elif v < dict_b[k]:
            ctr += (dict_b[k] - v)

for k, v in dict_b.items():
    if k not in dict_a:
        ctr += dict_b[k]

print(ctr)
