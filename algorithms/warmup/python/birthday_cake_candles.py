n = int(input())
candles = [int(c) for c in input().strip().split(' ')]

print(candles.count(max(candles)))
