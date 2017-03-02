def insertion_sort(arr):
    i = 1
    for _ in range(len(arr)):
        try:
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
            i += 1
            print(" ".join(str(x) for x in arr))
        except IndexError:
            pass

if __name__ == "__main__":
    size, arr = int(input()), [int(x) for x in input().strip().split(' ')]
    insertion_sort(arr)
