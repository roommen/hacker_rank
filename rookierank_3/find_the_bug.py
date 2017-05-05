
n = int(input().strip())
grid = []

for grid_i in range(n):
    grid_t = str(input().strip())
    if 'X' in grid_t:
        c = grid_t.index('X')
        r = grid_i
        print("{},{}".format(r, c))
        break
