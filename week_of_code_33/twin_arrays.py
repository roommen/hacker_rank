n = int(input())

A = [int(x) for x in input().split(' ')]
B = [int(x) for x in input().split(' ')]

A_copy, B_copy = A, B
# print(A_copy, B_copy)
minA, minB = min(A_copy), min(B_copy)
# print(minA, minB)
global_min = 999999999
try:
    while A.index(minA) == B.index(minB):
        if minA > minB:
            A_copy.pop(A.index(minA))
        elif minB > minA:
            B_copy.pop(B.index(minB))
        else:
            A_copy.pop(A.index(minA))
            B_copy.pop(B.index(minB))

        new_min = minA + minB
        # print(new_min)
        if new_min < global_min:
            global_min = new_min

        minA, minB = min(A_copy), min(B_copy)
    else:
        new_min = minA + minB
        # print(new_min)
        if new_min < global_min:
            global_min = new_min

    print(global_min)
except ValueError:
    # print(global_min)
    new_min = minA + minB
    if new_min < global_min:
        global_min = new_min

    print(global_min)
