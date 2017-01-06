import math
s = input()
sm = s.replace(" ", "")
r = math.floor(math.sqrt(len(sm)))
c = math.ceil(math.sqrt(len(sm)))
for i in range(c):
    print(sm[i::c], end=" ")
