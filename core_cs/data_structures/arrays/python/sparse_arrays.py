N = int(input())
word_dict = {}

for _ in range(N):
    word = input().strip()
    if word in word_dict:
        val = word_dict[word]
        word_dict[word] = val + 1
    else:
        word_dict[word] = 1

Q = int(input())
for _ in range(Q):
    query = input()
    if query in word_dict:
        print(word_dict[query])
    else:
        print(0)
