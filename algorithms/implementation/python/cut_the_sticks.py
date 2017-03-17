n = int(input().strip())

sticks = [int(x) for x in input().strip().split(' ')]
sticks_dup = sticks

while len(sticks_dup) != 0:
    print(len(sticks_dup))
    sticks_dup = []
    for x in sticks:
        y = x - min(sticks)
        if y != 0:
            sticks_dup.append(y)
    sticks = sticks_dup
