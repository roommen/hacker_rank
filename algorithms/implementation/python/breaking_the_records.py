n = int(input())

score = [int(s) for s in input().strip().split(' ')]

best = worst = score[0]

best_record, worst_record = 0, 0
for s in score[1:]:
    if s > best:
        best = s
        best_record += 1
    if s < worst:
        worst = s
        worst_record += 1

print(best_record, worst_record)
