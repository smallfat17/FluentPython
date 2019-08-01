#理解函数闭包

#类方式实现平均计算器
class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

def get_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager

def f1():
    count = 0
    def f2():
        nonlocal count
        count += 1
        return count
    return f2


if __name__ == '__main__':
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12),'\n')

    avg2 = get_averager()
    print(avg2.__code__.co_varnames)  #('new_value', 'total')
    print(avg2.__code__.co_freevars) #('series',)
    print(avg2(10))
    print(avg2(11))
    print(avg2(12))
    print(avg2.__closure__[0].cell_contents)

    f = f1()
    print(f())
    print(f())
    print(f())

    import dis
    print(dis.dis(f))