class Quantity:

    print('................??')
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        if instance is None:
            print('get none')
            return ('none')
        else:
            return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('Value must > 0')


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def test(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass

    def __init__(self, *args, **kwargs):
        d = dict(zip(self.__slots__, args))
        d.update(kwargs)
        for key, value in d.items():
            setattr(self, key, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ','.join('{!r}={!r}'.format(*i) for i in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attr = dict(__slots__ = field_names,
                    __init__ = __init__,
                    __repr__ = __repr__,
                    __iter__ = __iter__)

    return type(cls_name, (object,), cls_attr)

if __name__ == '__main__':
    # pass
    l = LineItem('smallfat', 20, 5)
    # print(l.weight)
    # print(LineItem.weight)
    # print(l.subtotal())
    # l.weight = 50
    # print(l.subtotal())

    # q = Quantity('smallfat')
    # q.data = 'ss'
    # print(q.data)

    # Person = test('Person', 'name age')
    # p = Person('jack', 25)
    # print(p)
