n = input().strip()
i = 0
prime = list()

while i < int(n):
    prime.append(input())
    i += 1


def is_prime(p):
    isprime = 1
    if int(p) == 1:
        isprime = 0
    else:
        j = 2
        from math import sqrt
        sq = sqrt(p)
        while j <= sq:
            if p % j == 0:
                isprime = 0
                break
            j += 1

    if isprime == 0:
        return "Not prime"
    elif isprime == 1:
        return "Prime"

for p in prime:
    print(is_prime(int(p)))
