g = int(input().strip())

for _ in range(g):
    n = int(input().strip())
    A = [int(a) for a in input().strip().split(' ')]

    if sorted(A) == A:
        print('ANDY' if len(A) % 2 == 0 else 'BOB')
    else:
        game_play = 0
        while len(A) != 0:
            new_A = A[:A.index(max(A))]
            A = new_A
            game_play += 1

        print('ANDY' if game_play % 2 == 0 else 'BOB')
