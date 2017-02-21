s = str(input().strip())

cosmic_change = 0
checker = 0

for x in s:
    checker += 1
    if x != "S" and checker == 1:
        cosmic_change += 1
    if x != "O" and checker == 2:
        cosmic_change += 1
    if x != "S" and checker == 3:
        cosmic_change += 1
    if checker == 3:
        checker = 0

print(cosmic_change)
