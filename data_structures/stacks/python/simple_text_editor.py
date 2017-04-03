undo_list = list()
s = ""


def simple_text_editor(ops_):
    global undo_list, s
    # Append 1st arg to end of string
    if ops_[0] == '1':
        new_str = s + ops_[1]
        s = new_str
        undo_list.append(new_str)
    # Delete the last k chars of S
    if ops_[0] == '2':
        k = int(ops_[1])
        new_str = s[:-k]
        s = new_str
        undo_list.append(new_str)
    # print the kth char of S
    if ops_[0] == '3':
        k = int(ops_[1])
        print(s[k-1])
    # Undo the last op of type 1 or 2, reverting S to the state it was in prior to that operation
    if ops_[0] == '4':
        undo_pop = undo_list.pop()
        if len(undo_list) != 0:
            s = undo_list[-1]
        else:
            s = ""


if __name__ == '__main__':
    Q = int(input())
    ctr = 0
    for _ in range(Q):
        ops = [o for o in input().strip().split(' ')]
        simple_text_editor(ops)
        ctr += 1

