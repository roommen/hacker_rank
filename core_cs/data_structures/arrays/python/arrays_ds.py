n = int(input())
arr = [int(a) for a in input().strip().split(' ')]

i = 1
for rev in arr:
    print(arr[-i], end=" ")
    i += 1
