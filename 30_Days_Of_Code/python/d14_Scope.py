class Difference:
    maximumDifference = 0

    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        maxno = max(self.__elements)
        minno = min(self.__elements)
        self.maximumDifference = abs(minno - maxno)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

_ = input()
a = [int(e) for e in input().split(' ')]

e = Difference(a)
e.computeDifference()
print(e.maximumDifference)
