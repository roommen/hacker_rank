n, k = map(int, input().strip().split(' '))
T = [int(t) for t in input().strip().split(' ')]

page = 1
book = dict()
for t in T:
    if t < k:
        book[page] = [int(x) for x in range(1, t+1)]
        page += 1
    else:
        q = t // k
        r = t % k
        j = 1
        l = k
        for i in range(0, q):
            book[page+i] = [int(x) for x in range(j, l+1)]
            j = l+1
            l += k
        page += q
        if r:
            l -= k
            book[page] = [int(x) for x in range(l + 1, l + r + 1)]
            page += 1

special = 0
for k, v in book.items():
    if k in v:
        special += 1

print(special)
