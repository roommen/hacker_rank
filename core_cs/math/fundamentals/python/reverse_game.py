T = int(input())

for _ in range(T):
    N, K = map(int, input().split(' '))
    i = 0
    final_list = list()
    while i <= N // 2:
        final_list.append(str((N-1) - i))
        final_list.append(str(i))
        i += 1

    if (N-1) % 2 == 0:
        new_list = final_list[:-1]
        print(list(new_list).index(str(K)))
    else:
        print(list(final_list).index(str(K)))
