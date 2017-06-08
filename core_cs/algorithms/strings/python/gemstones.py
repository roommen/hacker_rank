# First attempt #

# N = int(input())
#
# elements = list()
# for _ in range(N):
#     composition = {str(x) for x in input().strip()}
#     elements.append(list(composition))
#
# min_ = min(elements)
# elements.remove(min_)
#
# gem = 0
# for e in min_:
#     presence = 0
#     for i in range(len(elements)):
#         if e in elements[i]:
#             presence += 1
#     if presence == len(elements):
#         gem += 1
#
# print(gem)


# Second optimization #
# N = int(input())
# composition = [set(input()) for _ in range(N)]
#
# gems = set.intersection(*composition)
# print(len(gems))


# One-liner code golf
print(len(set.intersection(*[set(input()) for _ in range(int(input()))])))
