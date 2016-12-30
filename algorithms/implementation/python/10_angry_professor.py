n = input().strip()
ctr = 0

total_students = list()
min_students = list()
arrival_time = list()

while ctr < int(n):
    ts, ms = input().strip().split(' ')
    total_students.append(ts)
    min_students.append(ms)

    at = input().strip().split(' ')
    arrival_time.append(at)

    ctr += 1

ctr = 0
while ctr < len(total_students):
    threshold = 0
    for single_arrival_time in arrival_time[ctr]:
        if int(single_arrival_time) <= 0:
            threshold += 1

    if threshold >= int(min_students[ctr]):
        print('NO')
    else:
        print('YES')

    ctr += 1
