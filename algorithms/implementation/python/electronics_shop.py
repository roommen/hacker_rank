s, n, m = map(int, input().strip().split(' '))

kbs = [int(k) for k in input().strip().split(' ')]
usbs = [int(u) for u in input().strip().split(' ')]

# import time
# start_time = time.time()

spend = -1

for kb in kbs:
    for usb in usbs:
        value = usb + kb
        if (value <= s) and (spend <= value):
            spend = max(spend, value)

print(spend)

# print("--- %s seconds ---" % (time.time() - start_time))
