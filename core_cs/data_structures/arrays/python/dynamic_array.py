N, Q = map(int, input().strip().split(' '))
lastAns = 0
seqList = [list() for _ in range(N)]

for _ in range(Q):
    args = [int(arg) for arg in input().split(' ')]
    x = args[1]
    y = args[2]
    if args[0] == 1:
        seq = (x ^ lastAns) % N
        seqList[seq].append(y)
    if args[0] == 2:
        seq = (x ^ lastAns) % N
        size = len(seqList[seq])
        lastAns = seqList[seq][y % size]
        print(lastAns)
