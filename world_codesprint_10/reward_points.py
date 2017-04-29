if __name__ == '__main__':
    m1, m2, m3 = map(int, input().strip().split(' '))
    total = (100 if m1 >= 10 else m1 * 10) + (100 if m2 >= 10 else m2 * 10) + (100 if m3 >= 10 else m3 * 10)
    print(total)
