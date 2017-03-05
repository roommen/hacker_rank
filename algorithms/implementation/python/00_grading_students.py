def calc_grade(grade):
    if grade < 38:
        return grade
    else:
        mod_10 = grade % 10
        if mod_10 in [0, 1, 2, 5, 6, 7]:
            return grade
        if mod_10 in [3, 4]:
            return grade + (5 - mod_10)
        if mod_10 in [8, 9]:
            return grade + (10 - mod_10)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(calc_grade(int(input())))
