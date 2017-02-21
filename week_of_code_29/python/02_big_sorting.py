n = int(input().strip())

unsorted_list = list()
for _ in range(n):
    unsorted_list.append(int(input().strip()))

for x in sorted(unsorted_list):
    print(x)
