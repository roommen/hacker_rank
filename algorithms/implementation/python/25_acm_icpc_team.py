n, m = map(int, input().strip().split(' '))
bin_list = []

for _ in range(n):
    bin_list.append(input())

i = 1
all_knows = list()
for x in bin_list:
    for y in bin_list[i:]:
        all_knows.append(str(bin(int(x, 2) | int(y, 2)))[2:].count('1'))
    i += 1

print(max(all_knows))
print(all_knows.count(max(all_knows)))
