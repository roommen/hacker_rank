n = int(input())

A = [int(x) for x in input().split(' ')]
B = [int(x) for x in input().split(' ')]

i, min_, sum_ = 0, 99999999, 0
minA, minB = min(A), min(B)
if A.index(minA) != B.index(minB):
    print(minA+minB)
    # sortA = sorted(A)
    # print(sortA)
else:
    # sortA = sorted(A)
    # sortB = sorted(B)
    # i = 0
    # while A.index(sortA[i]) == B.index(sortB[i]):
    #     sortA.pop(i)
    #     sortB.pop(i)
    #     i += 1
    # print(sortA[i-1] + sortB[i-1])

    while i < n:
        j = 0
        while j < n:
            if i != j:
                sum_ = A[i] + B[j]
                if sum_ < min_:
                    min_ = sum_
            j += 1
        i += 1

    print(min_)
