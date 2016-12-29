# import sys

def memoize(f):
    cache = {}

    def fact(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return fact

@memoize
def factorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(int(input())))
