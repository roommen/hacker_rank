if __name__ == '__main__':
    score_name_dict = dict()
    score_list = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_name_dict[name] = score
        score_list.append(score)

    min_score = min(score_list)
    while min_score in score_list:
        score_list.pop(score_list.index(min_score))

    min_score = min(score_list)
    second_high_scores = list()

    for k, v in score_name_dict.items():
        if v == min_score:
            second_high_scores.append(k)

    for names in sorted(second_high_scores):
        print(names)
