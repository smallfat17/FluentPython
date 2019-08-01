import math
import itertools
import reprlib
import array
import numbers

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array.array(self.typecode, components)

    def __iter__(self):
        return (x for x in self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        return '{cls.__name__} ({components})'.format(cls=type(self), components=components[components.find('['):])

    def __abs__(self):
        return math.sqrt(sum((x**2 for x in self)))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            paris = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in paris)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(x * scalar for x in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

class B(list):
    def __add__(self, other):
        return other + ['a']

if __name__ == '__main__':
    v3 = Vector((3, 4))+ Vector((4, 5))
    print(v3)
    print(v3 + (3, 1, 0) + (1, 1, 1))
    print((2, 3, 4) + v3)
    # print(v3 + '123')
    print(v3 * 5)
    print(2 * v3 * 5)
    # print(v3 * 'a')
    print(divmod(10, 3))
    print(v3  @  v3*2)
    v3_alias = v3
    print(id(v3_alias), id(v3))

    b = B()
    print(b + list('ABC'))
