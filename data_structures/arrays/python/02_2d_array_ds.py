matrix = list()

for _ in range(6):
    line = [int(val) for val in input().strip().split(' ')]
    matrix.append(line)

i, j, k = 0, 1, 2
i1, i2 = 0, 3
j1 = 1
line = list()
for _ in range(4):
    for _ in range(4):
        line1 = [int(l1) for l1 in matrix[i][i1:i2]]
        line2 = matrix[j][j1]
        line3 = [int(l3) for l3 in matrix[k][i1:i2]]
        i1 += 1
        i2 += 1
        j1 += 1
        line_sum = sum(line1) + line2 + sum(line3)
        line.append(line_sum)
    i += 1
    j += 1
    k += 1
    i1, i2 = 0, 3
    j1 = 1

print(max(line))
