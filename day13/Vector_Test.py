import array
import reprlib
import math
import numbers
import operator
import functools
import itertools

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'
    __slots__ = ['_components', 'X']

    def __init__(self, components):
        self._components = array.array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        cls = type(self)

        components = reprlib.repr(self._components)
        components = components[components.find('['): -1]
        return '{.__name__!r} ({})'.format(cls ,components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])+
                bytes(self._components))

    def __hash__(self):
        return functools.reduce(operator.xor, map(hash, self), 0)

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __abs__(self):
        return math.sqrt(sum(x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    #序列协议
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)

        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos <len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, key, value):
        cls = type(self)

        if len(key) == 1:
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = 'can\'t set attribute \'a\' to \'z\' in {cls.__name__!r}'
            else:
                error = ''
            if error:
                msg = error.format(cls=cls, attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):  # 超球面坐标
            fmt_spec = fmt_spec[:-1]

            coords = itertools.chain([abs(self)],
                                 self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))


class Student:
    def speak(self):
        print('hello')

class Person(Student, Vector):pass

if __name__ == '__main__':
    v1 = Vector(range(10))
    print(repr(v1))
    v2 = Vector([4, 5, 6])
    print(abs(v2))

    v3 = Vector.frombytes(bytes(v1))
    print(v3)
    print(v1 == v3)
    print(repr(v2))

    v4 = v1[2:8:3]
    print(repr(v4)) #Vector ([2.0, 5.0])
    print(v4.__class__)
    print(v1)
    #v1.x = 10  #定义了__setter__后报错 readonly attribute 'x'
    print(v1.x)
    print(v1) # (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0) 没有改变

    #v1.s = 'a' #can't set attribute 'a' to 'z' in 'Vector'
    # p = Person([1, 2, 3])
    # print(repr(p))
    v1.X = '111'
    print(hash(v1))
    print(hash(v2))
    print(format(v1, 'h'))









