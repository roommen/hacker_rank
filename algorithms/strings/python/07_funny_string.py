n = input()
not_funny = 1
for _ in range(int(n)):
    s = input()
    r = s[::-1]
    i = 1
    while not_funny and i < len(s):
        if abs(ord(s[-i]) - ord(s[-(i+1)])) == abs(ord(r[-i]) - ord(r[-(i+1)])):
            pass
        else:
            not_funny = 0
            print('Not Funny')
        i += 1

    if not_funny == 1:
        print('Funny')

    not_funny = 1
