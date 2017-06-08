n = int(input().strip())

letters = "abcdefghijklmnopqrstuvwxyz"

for _ in range(n):
    s = str(input().strip())
    unique = set()
    for letter in letters:
        if letter in s:
            unique.add(letter)

    print(len(unique))
