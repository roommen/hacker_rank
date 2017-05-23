year = int(input().strip())

if 1700 <= year <= 1917:
    if year % 4 == 0:
        # Days in the first 8 months = 31+29+31+30+31+30+31+31 = 244
        print("{}.09.{}".format(256-244, year))
    else:
        # Days in the first 8 months = 31+28+31+30+31+30+31+31 = 243
        print("{}.09.{}".format(256-243, year))
elif year == 1918:
    # Days in the first 8 months = 31+15+31+30+31+30+31+31
    print("{}.09.{}".format(256-230, year))
elif 1919 <= year <= 2700:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        # Days in the first 8 months = 31+29+31+30+31+30+31+31 = 244
        print("{}.09.{}".format(256 - 244, year))
    else:
        # Days in the first 8 months = 31+28+31+30+31+30+31+31 = 243
        print("{}.09.{}".format(256 - 243, year))
