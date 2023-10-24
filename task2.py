import random

# cafe 1, 2, 3, 4
# mean
#
c1Mean = 7
c2Mean = 4
c3Mean = 10
c4Mean = 5

c1Dev = 3
c2Dev = 10
c3Dev = 6
c4Dev = 2


def exploreOnly() -> float:
    visits = 50
    happiness = 0
    for i in range(visits):
        c1 = random.normalvariate(c1Mean, c1Dev)
        c2 = random.normalvariate(c2Mean, c2Dev)
        c3 = random.normalvariate(c3Mean, c3Dev)
        c4 = random.normalvariate(c4Mean, c4Mean)
        happiness += c1
        happiness += c2
        happiness += c3
        happiness += c4
    return ("%.2f" % happiness)


x = exploreOnly()
print(x)
