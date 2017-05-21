vowels = "aeiouy"


def beautiful_word(word_):
    i = 0
    try:
        while i < len(word):
            if (word[i] == word[i+1]) or (word[i] in vowels and word[i+1] in vowels):
                return 'No'
            i += 1
        return 'Yes'
    except IndexError:
        return 'Yes'


if __name__ == '__main__':
    word = str(input())
    print(beautiful_word(word))
