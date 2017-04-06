def fibonacci(N_):
    even_nums = [2]
    i, j = 1, 2
    new_fib = 0
    while new_fib <= N_:
        new_fib = i + j
        i = j
        j = new_fib
        if new_fib % 2 == 0 and new_fib < N_:
            even_nums.append(new_fib)

    return sum(even_nums)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        even_sum = fibonacci(N)
        print(even_sum)
