#!/bin/python3

# import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


final_first_row = []
final_second_row = []
final_third_row = []
sum_final = []

for x in arr[:4]:
    first_row = x
    i = 0
    k = 3
    while i < 4:
        three_first_row = first_row[i:k]
        final_first_row.append(three_first_row)
        i += 1
        k += 1

ctr = 0
for y in arr[1:5]:
    second_row = y
    i = 1
    while i < 5:
        single_second_row = second_row[i]
        final_second_row.append(single_second_row)
        i += 1

ctr = 0
for z in arr[2:6]:
    third_row = z
    i = 0
    k = 3
    while i < 4:
        three_first_row = third_row[i:k]
        final_third_row.append(three_first_row)
        i += 1
        k += 1

i = 0
while i < 16:
    a = sum(final_first_row[i]) + final_second_row[i] + sum(final_third_row[i])
    sum_final.insert(i, a)
    i += 1

print(max(sum_final))
