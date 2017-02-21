s = input().strip()

itsCaps = 0
for x in s:
    # print(ord(x))
    if ord(x) == ord(str(x).capitalize()):
        itsCaps += 1

print(itsCaps+1)
