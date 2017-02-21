alphabets = "abcdefghijklmnopqrstuvwxyz"

s = str(input().strip())
letter_count = 0
for x in alphabets:
    if x in s.lower():
        letter_count += 1

print("pangram" if letter_count == 26 else "not pangram")
