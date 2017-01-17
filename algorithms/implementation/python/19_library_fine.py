import datetime

ad, am, ay = input().strip().split(' ')
ed, em, ey = input().strip().split(' ')

act_date = datetime.date(day=int(ad), month=int(am), year=int(ay))
exp_date = datetime.date(day=int(ed), month=int(em), year=int(ey))

if act_date <= exp_date:
    print(0)

elif int(ay) != int(ey):
    print(10000)

elif int(ad) != int(ed):
    if int(am) == int(em):
        print(15 * (int(ad) - int(ed)))
    else:
        print(500 * (int(am) - int(em)))

elif int(am) != int(em):
    if int(ay) == int(ey):
        print(500 * (int(am) - int(em)))
