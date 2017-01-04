from functools import lru_cache

@lru_cache(1000)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(int(input())))
