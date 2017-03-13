# Solution taken from discussion

n, m = map(int, input().strip().split(' '))
stations = sorted(int(station) for station in input().split())

# initialize with ends
maximum = max(stations[0], n - stations[-1] - 1)
for i in range(1, m):
    d = stations[i] - stations[i-1]
    maximum = max(d//2, maximum)

print(maximum)
