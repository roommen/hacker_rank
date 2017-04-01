from functools import reduce

n, A = int(input()), [int(x) for x in input().strip().split(' ')]

# for x in A:
#     # print(A.count(x))
#     if A.count(x) % 2 != 0:
#         print(" ".join(str(x)))

answer = reduce((lambda x, y: x ^ y), A)
print(answer)

