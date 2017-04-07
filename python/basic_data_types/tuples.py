n = int(input())

list_n = [int(x) for x in input().strip().split(' ')]

print(hash(tuple(list_n)))
