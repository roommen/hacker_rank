if __name__ == '__main__':
    n = int(input().strip())
    S = [int(s) for s in input().strip().split(' ')]
    d, m = map(int, input().strip().split(' '))

    ways, i = 0, 0
    len_ = len(S)
    try:
        while i < len_:
            j, sum_ = 0, 0
            while j < m:
                sum_ += S[i+j]
                j += 1
            if sum_ == d:
                ways += 1
            i += 1
        print(ways)
    except IndexError:
        print(ways)
