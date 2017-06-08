# Implementing custom Counter

# a = str(input())
# b = str(input())
#
# a_dict = dict()
# b_dict = dict()
#
# for str_ in a:
#     if str_ not in a_dict:
#         a_dict[str_] = a.count(str_)
#
# for str_ in b:
#     if str_ not in b_dict:
#         b_dict[str_] = b.count(str_)
#
# unique_dict = dict()
# for k in a_dict.keys():
#     if k not in unique_dict:
#         if k in b_dict:
#             unique_dict[k] = abs(a_dict[k] - b_dict[k])
#         else:
#             unique_dict[k] = a_dict[k]
#
# for k in b_dict.keys():
#     if k not in unique_dict:
#         unique_dict[k] = b_dict[k]
#
# deletions = 0
# for v in unique_dict.values():
#     deletions += v
#
# print(deletions)

# Using inbuilt Counter
from collections import Counter
a = Counter(input().strip())
b = Counter(input().strip())

print(int(sum((a-b).values())) + int(sum((b-a).values())))
