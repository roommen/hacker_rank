n = int(input().strip())

consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiou"

melodious_password = set()

if n == 1:
    for c in consonants:
        print(c)
    for v in vowels:
        print(v)

if n == 2:
    for c in consonants:
        for v in vowels:
            print("{con}{vow}".format(con=c, vow=v))
    for v in vowels:
        for c in consonants:
            print("{vow}{con}".format(vow=v, con=c))

if n == 3:
    for c in consonants:
        for v in vowels:
            for c2 in consonants:
                print("{con}{vow}{con2}".format(con=c, vow=v, con2=c2))
    for v in vowels:
        for c in consonants:
            for v2 in vowels:
                print("{vow}{con}{vow2}".format(vow=v, con=c, vow2=v2))

if n == 4:
    for c in consonants:
        for v in vowels:
            for c2 in consonants:
                for v2 in vowels:
                    print("{con}{vow}{con2}{vow2}".format(con=c, vow=v, con2=c2, vow2=v2))
    for v in vowels:
        for c in consonants:
            for v2 in vowels:
                for c2 in consonants:
                    print("{vow}{con}{vow2}{con2}".format(vow=v, con=c, vow2=v2, con2=c2))

if n == 5:
    for c in consonants:
        for v in vowels:
            for c2 in consonants:
                for v2 in vowels:
                    for c3 in consonants:
                        print("{con}{vow}{con2}{vow2}{con3}".format(con=c, vow=v, con2=c2, vow2=v2, con3=c3))
    for v in vowels:
        for c in consonants:
            for v2 in vowels:
                for c2 in consonants:
                    for v3 in vowels:
                        print("{vow}{con}{vow2}{con2}{vow3}".format(vow=v, con=c, vow2=v2, con2=c2, vow3=v3))

if n == 6:
    for c in consonants:
        for v in vowels:
            for c2 in consonants:
                for v2 in vowels:
                    for c3 in consonants:
                        for v3 in vowels:
                            print("{con}{vow}{con2}{vow2}{con3}{vow3}".format(con=c, vow=v, con2=c2, vow2=v2, con3=c3, vow3=v3))
    for v in vowels:
        for c in consonants:
            for v2 in vowels:
                for c2 in consonants:
                    for v3 in vowels:
                        for c3 in consonants:
                            print("{vow}{con}{vow2}{con2}{vow3}{con3}".format(vow=v, con=c, vow2=v2, con2=c2, vow3=v3, con3=c3))

