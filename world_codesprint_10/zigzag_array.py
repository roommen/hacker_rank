def minimumDeletions(a):
    len_ = len(a)
    if len_ == 0:
        return 0
    i, ctr, recheck = 0, 0, 0
    try:
        while i < len_:
            if (a[i] < a[i+1] < a[i+2]) or (a[i] > a[i+1] > a[i+2]):
                a.pop(i+1)
                ctr += 1
                recheck = 1
                # print(a)
            if recheck == 0:
                i += 1
            else:
                recheck = 0
        return ctr
    except IndexError:
        return ctr


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Return the minimum number of elements to delete to make the array zigzag
result = minimumDeletions(a)
print(result)
