n, d = map(int, input().strip().split(' '))
arr = [int(x) for x in input().split(' ')]

" ".join(str(s) for s in arr[d:] + arr[0:d])
