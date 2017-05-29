stack = list()

class MyQueue(object):
    global stack

    def __init__(self):
        pass

    def peek(self):
        return stack[0]

    def pop(self):
        return stack.pop(0)

    def put(self, value):
        stack.append(value)

queue = MyQueue()
t = int(input())

for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
