def capitalize(string_):
    return " ".join((s.capitalize() for s in string_.split(' ')))

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
