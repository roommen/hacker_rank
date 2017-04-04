def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res


s_ = input()
t_ = input()
print(strings_xor(s_, t_))


# print(str(bin(int(input(), base=2) ^ int(input(), base=2)))[2:])
