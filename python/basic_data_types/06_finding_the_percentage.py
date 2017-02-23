if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = format(sum(scores) / len(scores), '.2f')
    query_name = input()
    print(student_marks[query_name])
