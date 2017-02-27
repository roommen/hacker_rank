size = int(input())
arr = [int(x) for x in input().strip().split(' ')]

v = arr[-1]
check_index = 2
shift_index = 1

try:
    while arr[-check_index] > v:
        arr[-shift_index] = arr[-check_index]
        shift_index += 1
        check_index += 1
        for s_val in arr:
            print(s_val, end=" ")
        print("")
    else:
        arr[len(arr) - shift_index] = v
        for s_val in arr:
            print(s_val, end=" ")
except IndexError:
    arr[len(arr) - shift_index] = v
    for s_val in arr:
        print(s_val, end=" ")
