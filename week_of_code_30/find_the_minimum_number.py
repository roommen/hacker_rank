if __name__ == '__main__':
    n = int(input().strip())
    final_string = "min(int, int)"
    print("min(int, " * (n-2) + final_string + ")" * (n-2))
