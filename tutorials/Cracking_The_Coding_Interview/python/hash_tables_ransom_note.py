m, n = map(int, input().strip().split(' '))

magazine = [word for word in input().strip().split(' ')]
ransom_note = [word for word in input().strip().split(' ')]

magazine_hash = {}
ransom_note_copy = list()


def create_magazine_hash():
    for word in magazine:
        if word not in magazine_hash:
            magazine_hash[word] = 1
        else:
            val = magazine_hash[word]
            magazine_hash[word] = val + 1


def ransom_note_checker():
    for word in ransom_note:
        if word in magazine_hash:
            val = magazine_hash[word]
            if val >= 1:
                magazine_hash[word] = val - 1
                ransom_note_copy.append(word)
            if val == 0:
                print("No")
                break
        else:
            print("No")
            break
    print(ransom_note, ransom_note_copy, create_magazine_hash)
    if ransom_note == ransom_note_copy:
        print("Yes")

create_magazine_hash()
ransom_note_checker()
