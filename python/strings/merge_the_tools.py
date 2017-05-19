# Taken from the discussion section - solution by FJSevilla

S, N = input(), int(input())
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([d.setdefault(c, c) for c in part if c not in d]))
