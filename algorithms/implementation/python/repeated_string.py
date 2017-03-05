s, n = input().strip(), int(input().strip())

ctr1 = s.count('a') * (n // len(s))
ctr2 = s[:n % len(s)].count('a')

print(ctr1 + ctr2)
