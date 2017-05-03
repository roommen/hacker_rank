if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    A = [int(a) for a in input().strip().split(' ')]

    i = 0
    divisible = 0
    while i < n:
        j = i+1
        while j < n:
            if (A[i] + A[j]) % k == 0:
                divisible += 1
            j += 1
        i += 1

    print(divisible)
