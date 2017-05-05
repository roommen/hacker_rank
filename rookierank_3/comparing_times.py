#!/bin/python3

# import datetime

def timeCompare(t1, t2):
    ampm1 = t1[5:]
    ampm2 = t2[5:]

    time1 = t1[:5]
    time2 = t2[:5]

    hr1, m1 = time1.split(':')
    hr2, m2 = time2.split(':')

    if ampm1 == 'PM':
        if int(hr1) == 12:
            newhr1 = int(hr1)
        else:
            newhr1 = int(hr1) + 12
    else:
        if int(hr1) == 12:
            newhr1 = 0
        else:
            newhr1 = int(hr1)

    if ampm2 == 'PM':
        if int(hr2) == 12:
            newhr2 = int(hr2)
        else:
            newhr2 = int(hr2) + 12
    else:
        if int(hr2) == 12:
            newhr2 = 0
        else:
            newhr2 = int(hr2)

    time_1 = str(newhr1) + str(m1)
    time_2 = str(newhr2) + str(m2)

    if int(time_1) > int(time_2):
        return 'Second'
    else:
        return 'First'


q = int(input().strip())
for a0 in range(q):
    t1, t2 = input().strip().split(' ')
    t1, t2 = [str(t1), str(t2)]
    result = timeCompare(t1, t2)
    print(result)
