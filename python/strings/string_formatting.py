def print_formatted(number):
    width_bin = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(width_bin, ' '), oct(i)[2:].rjust(width_bin, ' '), hex(i)[2:].upper().rjust(width_bin, ' '),
              bin(i)[2:].rjust(width_bin, ' '), sep=' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
