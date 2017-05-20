s = "0"

while len(s) <= 1000:
    t = ""
    for s_ in s:
        if s_ == "0":
            t += "1"
        else:
            t += "0"
    s_expand = s + t
    s = s_expand

q = int(input())

for _ in range(q):
    x = int(input())
    print(s[x])
