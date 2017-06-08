def super_digit(s_digit):
    if len(str(s_digit)) == 1:
        return s_digit

    sum_ = 0
    for s in str(s_digit):
        sum_ += int(s)
    return super_digit(sum_)


if __name__ == '__main__':
    n, k = map(str, input().split(' '))
    sum_ = 0
    if int(k) > 1:
        for n_ in n:
            sum_ += int(n_)
    print(super_digit(sum_ * k))
