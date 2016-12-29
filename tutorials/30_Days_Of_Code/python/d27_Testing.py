print(5)
print(5, 3)
print(-1, 90, 999, 100, 0)
print(4, 2)
print(0, -1, 2, 1)
print(3, 3)
print(-1, 0, 1)
print(6, 1)
print(-1, 0, 1, -1, 2, 3)
print(7, 3)
print(-1, 0, 1, 2, 3, 4, 5)

# The program which you can use to verify the output of 'YES' or 'NO'
# This is not required as part of the solution and hence commented out

# n = input().strip()
# ctr = 0
#
# total_students = list()
# min_students = list()
# arrival_time = list()
#
# while ctr < int(n):
#     ts, ms = input().strip().split(' ')
#     total_students.append(ts)
#     min_students.append(ms)
#
#     at = input().strip().split(' ')
#     arrival_time.append(at)
#
#     ctr += 1
#
# ctr = 0
# while ctr < len(total_students):
#     threshold = 0
#     for single_arrival_time in arrival_time[ctr]:
#         if int(single_arrival_time) <= 0:
#             threshold += 1
#
#     if threshold >= int(min_students[ctr]):
#         print('NO')
#     else:
#         print('YES')
#
#     ctr += 1
