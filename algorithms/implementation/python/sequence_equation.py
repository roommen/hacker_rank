n = int(input())
x_list = [int(x) for x in input().strip().split(' ')]

index_ = 1
x_dict = dict()
for x in x_list:
    x_dict.setdefault(index_, x)
    index_ += 1

key_ = 0
for n_ in range(1, n+1):
    for k, v in x_dict.items():
        if v == n_:
            key_ = k
    for k, v in x_dict.items():
        if v == key_:
            print(k)
