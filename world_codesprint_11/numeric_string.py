s = str(input())
k, b, m = map(int, input().split(' '))

len_ = len(s)

i = 0
mod_sum = 0
while (len_ - i) >= k:
    num = s[i:(i+k)]
    baseb = int(num, base=b)
    base10 = int(str(baseb), base=10)
    mod = base10 % m
    mod_sum += mod
    i += 1

print(mod_sum)
