n, d = map(int, input().strip().split(' '))
arr = [int(x) for x in input().strip().split(' ')]

# O(n) solution
# arr2 = arr
# for _ in range(d):
#     arr2 = arr
#     #print(arr, arr2)
#     l = len(arr2)
#     arr2.insert(l, arr[0])
#     #print(arr2)
#     arr = arr2[1:]
#

# O(1) solution
arr2 = list()
arr2 = arr[d:] + arr[:d]

for x in arr2:
    print(x, "", end="")
