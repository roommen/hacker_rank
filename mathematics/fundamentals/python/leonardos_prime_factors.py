first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137]

q = int(input().strip())

for _ in range(q):
    n = int(input().strip())
    if n == 1:
        print(0)
    prod = 1
    i = 0
    primes = 0
    if n > 1:
        while prod <= n:
            prod *= first_primes[i]
            i += 1
            primes += 1
        print(primes-1, first_primes[i-1])
