T = int(input().strip())

for _ in range(T):
    n = int(input())

    # O(n) solution
    # k, sum_ = 1, 0
    # while k <= n:
    #     tn = k**2 - ((k-1)**2)
    #     sum_ += tn
    #     k += 1

    # O(1) solution
    sum_ = (n % 1000000007) ** 2

    print(sum_ % 1000000007)
