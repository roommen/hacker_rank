N = int(input())

stack = list()
max_stack = list()
max_ = 0
for _ in range(N):
    args = [int(arg) for arg in input().split(' ')]
    if args[0] == 1:
        stack.append(args[1])
        if len(max_stack) == 0 or args[1] >= max_stack[-1]:
            max_stack.append(args[1])
    if args[0] == 2:
        item_pop = stack.pop()
        if len(max_stack) > 0:
            if max_stack[-1] == item_pop:
                max_stack.pop()
    if args[0] == 3:
        if len(max_stack) > 0:
            print(max_stack[-1])
