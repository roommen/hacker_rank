mins = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 21: "twenty one", 22: "twenty two", 23: "twenty three", 24: "twenty four", 25: "twenty five", 26: "twenty six", 27: "twenty seven",
        28: "twenty eight", 29: "twenty nine"}

h = input().strip()
m = input().strip()

if int(m) == 0:
    print(mins.__getitem__(int(h)), 'o\' clock')

if int(m) == 1:
    print(mins.__getitem__(int(m)), 'minute past', mins.__getitem__(int(h)))

if 2 <= int(m) <= 14:
    print(mins.__getitem__(int(m)), 'minutes past', mins.__getitem__(int(h)))

if int(m) == 15:
    print('quarter past', mins.__getitem__(int(h)))

if 16 <= int(m) <= 29:
    print(mins.__getitem__(int(m)), 'minutes past', mins.__getitem__(int(h)))

if int(m) == 30:
    print('half past', mins.__getitem__(int(h)))

if 31 <= int(m) <= 44:
    print(mins.__getitem__(60 - int(m)), 'minutes to', mins.__getitem__(int(h) + 1))

if int(m) == 45:
    print('quarter to', mins.__getitem__(int(h) + 1))

if 46 <= int(m) <= 59:
    print(mins.__getitem__(60 - int(m)), 'minutes to', mins.__getitem__(int(h) + 1))
