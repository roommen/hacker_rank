if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    max_val = max(arr)
    while max_val in arr:
        arr.pop(arr.index(max_val))
    print(max(arr))
