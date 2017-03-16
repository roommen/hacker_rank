T = int(input())

for _ in range(T):
    N = int(input())
    password = [str(p) for p in input().strip().split(' ')]
    loginAttempt = str(input())

    i, j = 0, 0
    actual_password = list()
    while j <= len(loginAttempt):
        if loginAttempt[i:j] in password:
            actual_password.append(loginAttempt[i:j])
            i = j
        else:
            if j == len(loginAttempt):
                actual_password = []
                actual_password.append('WRONG PASSWORD')
        j += 1

    print(*actual_password)
