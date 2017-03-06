n, d = map(int, input().strip().split(' '))
numbers = [int(n) for n in input().strip().split(' ')]

beautiful_triplets = 0
for n in numbers:
    i, j, k = n, n+d, n+(2*d)
    if k > numbers[-1]:
        break
    if j in numbers and k in numbers:
        beautiful_triplets += 1

print(beautiful_triplets)
