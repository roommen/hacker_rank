# Taken from the discussion

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
d = {}
count = 0
selected = 0

for itm in a:
    count = d.get(itm, 0)
    count += 1
    d[itm] = count

    tmp1 = count + d.get(itm - 1, 0)
    tmp2 = count + d.get(itm + 1, 0)
    selected = max(tmp1, tmp2, selected)

print(selected)
