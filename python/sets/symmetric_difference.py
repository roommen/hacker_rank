M = int(input().strip())
M_set = {int(m) for m in input().strip().split(' ')}

N = int(input().strip())
N_set = {int(n) for n in input().strip().split(' ')}

symm_diff = list(M_set.difference(N_set)) + list(N_set.difference(M_set))

print(*sorted(symm_diff), sep="\n")
