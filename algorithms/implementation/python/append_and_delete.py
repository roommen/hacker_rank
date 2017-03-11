s = [i for i in input().strip()]
t = [i for i in input().strip()]
k = int(input().strip())

if len(t) < len(s):
    end = len(t)
else:
    end = len(s)
index = end

for i in range(end):
    if s[i] != t[i]:
        index = i
        break

remove = len(s) - index
append = len(t) - index

if remove + append <= k and (k-(remove+append)) % 2 == 0:
    print("Yes")
elif k >= len(s) + len(t):
    print("Yes")
else:
    print("No")
