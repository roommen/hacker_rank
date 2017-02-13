#!/bin/python3
n = int(input().strip())
value = 0
fib_dict = {}


def fibonacci(n):
    global value
    if n in fib_dict:
        return fib_dict[n]
    if n == 1:
        value = 1
    if n == 2:
        value = 1
    if n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fib_dict[n] = value
    return value

print(fibonacci(n))
