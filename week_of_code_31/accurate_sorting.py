if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        A = [int(a) for a in input().strip().split(' ')]

        i = 0
        try:
            while i < n:
                if (abs(A[i] - A[i+1]) == 1) and (A[i] > A[i+1]):
                    A[i], A[i+1] = A[i+1], A[i]
                i += 1
        except IndexError:
            pass

        if min(A) == A[0] and max(A) == A[n-1]:
            print('Yes')
        else:
            print('No')
