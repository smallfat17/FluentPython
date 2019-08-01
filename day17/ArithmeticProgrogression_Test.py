from fractions import Fraction

class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)# 2+2.5 3 _>float(3)   1+2 3->>int(3)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

if __name__ == '__main__':
    ar = ArithmeticProgression(0, Fraction(1, 5))
    for a in ar:
        print(a)

    import itertools
    itertools.permutations()
    

