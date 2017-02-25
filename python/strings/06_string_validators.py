if __name__ == '__main__':
    s = str(input())
    alnum, alpha, digit, low, up = 0, 0, 0, 0, 0
    for string in s:
        if alnum == 0:
            if string.isalnum():
                alnum = 1
        if alpha == 0:
            if string.isalpha():
                alpha = 1
        if digit == 0:
            if string.isdigit():
                digit = 1
        if low == 0:
            if string.islower():
                low = 1
        if up == 0:
            if string.isupper():
                up = 1
        if alnum == 1 and alpha == 1 and digit == 1 and low == 1 and up == 1:
            break

    print("True" if alnum == 1 else "False")
    print("True" if alpha == 1 else "False")
    print("True" if digit == 1 else "False")
    print("True" if low == 1 else "False")
    print("True" if up == 1 else "False")

