trips = int(input().strip())

for _ in range(trips):
    m = int(input().strip())  # m = 4
    n = int(input().strip())  # n = 5
    cost = [int(c) for c in input().strip().split(' ')]  # 1 4 5 3 2

    affordable_cost = [int(ac) for ac in sorted(cost) if int(ac) < m]  # 1 2 3

    dup_list = list()
    for ac in affordable_cost:
        if m - ac in affordable_cost:
            if cost.count(m-ac) > 1:
                for i in range(len(cost)):
                    if cost[i] == m-ac:
                        dup_list.append(i)
                print(*sorted([dup_list[0]+1, dup_list[1]+1]))
                break
            else:
                print(*sorted([cost.index(m - ac) + 1, cost.index(ac) + 1]))
                break
