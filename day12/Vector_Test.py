from array import array
import math

class Vector:
    typecode = 'd'
    __slots__ = ('__x', '__y', '__weakref__')

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self):
        return math.atan2(self.x, self.y)

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in(self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __bytes__(self):
        return (bytes([ord(self.typecode)])+
                bytes(array(self.typecode, self)))

    def __abs__(self):
        # return pow((self.x **2 + self.y **2), 0.5)
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            out_format = '<{}, {}>'
        else:
            coords = self
            out_format = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return out_format.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


def func():
    print('bye bye....')


class ShoterVector(Vector):
    typecode = 'f'

if __name__ == '__main__':
    v1 = Vector(3, 4)
    # print(v1)
    # x, y = v1
    # print(x, y)
    # v1_clone = eval(repr(v1))
    # print(v1_clone)
    # print(v1 == v1_clone)
    # print(bytes(v1))
    # print(abs(v1))
    # print(bool(v1), bool(Vector(0, 0)))
    #
    # v2 = Vector.frombytes(bytes(v1))
    # print(v2)
    # print(format(v1))
    # print(format(Vector(1, 1), '.5fp'))
    # print(format(v1, 'p'))
    #
    # s = {v1}
    # print(s)

    #私有属性
    # print(v1.__dict__) #{'_Vector__x': 3.0, '_Vector__y': 4.0}
    # v1._Vector__x = 10
    # print(v1)
    import weakref
    a = weakref.ref(v1) #__slots__中必须有__weakref__否则报错
    v3 = v1
    ender = weakref.finalize(v1, func)
    # del v1
    # print( 'v3',v3)
    # print(ender.alive)
    # del v3
    # print(ender.alive)
    # del a
    # print(ender.alive)

    sv = ShoterVector(3, 4)
    print(sv)
    print(abs(sv))
    print(bytes(sv))
    print(len(bytes(sv)))

    print(bytes(v1))
    print(len(bytes(v1)))


