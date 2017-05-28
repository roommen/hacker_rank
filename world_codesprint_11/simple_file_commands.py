file_names = list()
f_dict = dict()

q = int(input())

for _ in range(q):
    cmd, file = str(input()).split(' ')
    if cmd == 'crt':
        if file not in f_dict:
            f_dict[file] = [0]
        else:
            val_ = list(f_dict[file])
            max_ = max(val_)
            val_.append(max_+1)
            f_dict[file] = val_
        val_ = list(f_dict[file])
        if len(val_) == 1:
            print("+", file)
        else:
            print("+ {}({})".format(file, max(val_)))

    # file_index = ""
    if cmd == 'del':
        fname_split = file.split('(')
        # print("split", fname_split[0])
        if len(fname_split) == 1:
            print("- {}".format(file))
            val_ = list(f_dict[file])
            val_.remove(0)
            f_dict[file] = val_
        else:
            print("- {}".format(file))
            num = fname_split[1][-2::-1]
            print("num", num)
            val_ = list(f_dict[fname_split[0]])
            val_.remove(int(num))
            f_dict[fname_split[0]] = val_


    # print(f_dict)



