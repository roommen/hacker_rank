inp = int(input().strip())

i = 0

while i < inp:
    s = input()
    j = 0
    odd = 1
    even = 0
    es = ""
    os = ""

    while j < len(s):
        if even < len(s):
            es = es + s[even]
        if odd < len(s):
            os = os + s[odd]
        even += 2
        odd += 2
        j += 1
    print(es + " " + os)
    i += 1
