n = int(input())

arr_ = [int(a) for a in input().split(' ')]

len_ = len(arr_)

mid = len_ // 2

first_half = arr_[:mid]
second_half = arr_[mid:]

print(abs(sum(first_half) - sum(second_half)))
