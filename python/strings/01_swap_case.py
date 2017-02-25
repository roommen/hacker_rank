def swap_case(s):
    swap_s = ""
    for letter in s:
        if letter.islower():
            swap_s += letter.upper()
        else:
            swap_s += letter.lower()

    return swap_s

s = str(input().strip())

print(swap_case(s))
