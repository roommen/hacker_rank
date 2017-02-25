open_list = ['{', '[', '(']
closed_list = ['}', ']', ')']
stack = list()


def is_matched(expression):
    index = 0
    match = 0
    len_expr = len(expression)
    if expression[0] in closed_list or expression[-1] in open_list:
        return False
    for characters in expression:
        if characters in open_list:
            stack.append(characters)
            index += 1
        elif characters in closed_list:
            last_char = stack[-1]
            if characters == '}' and last_char == '{':
                stack.pop()
                match += 1
            elif characters == ']' and last_char == '[':
                stack.pop()
                match += 1
            elif characters == ')' and last_char == '(':
                stack.pop()
                match += 1
            else:
                return False
        if match == (len_expr//2):
            return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    print("YES" if is_matched(expression) else "NO")
