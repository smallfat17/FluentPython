from functools import reduce

#n的阶乘
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
print(fact(5))


#使用operator
import operator
def fact_operator(n):
    return reduce(operator.mul, range(1, n+1))
print(fact_operator(5))

#itemgetter
a = [0, 1, 2]
getter1 = operator.itemgetter(1)
print(getter1(a)) #1

#attrgetter
from collections import namedtuple
City = namedtuple('City', 'name country')
guangzhou = City('guangzhou', 'China')
attrgetter1 = operator.attrgetter('country')
print(attrgetter1(guangzhou)) #China

