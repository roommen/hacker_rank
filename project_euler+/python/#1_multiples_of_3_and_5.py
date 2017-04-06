# Iterative solution - O(N)
# def sum_multiples(N_):
#     multiples = {3}
#     i, increment = 3, 2
#     while i < N_:
#         j = i
#         j += increment
#         increment += 2
#         if j < N_:
#             multiples.add(j)
#         i += 3
#         if i < N_:
#             multiples.add(i)
#
#     return 1
#     # return sum(multiples)


# Optimal solution - O(1)
def sum_multiples(n, k):
    m = (k - 1) // n
    return n * m * (m + 1) // 2


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N < 3:
            print(0)
        else:
            print(sum_multiples(3, N) + sum_multiples(5, N) - sum_multiples(15, N))
