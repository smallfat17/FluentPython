import abc

class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        print('get description')
        if instance is None:
            return self
        else:
            return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        return super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        '''return validate value or raise ValueError'''


class Quantity(Validated):

    def validate(self, instance, value):
        if value > 0:
            return value
        else:
            raise ValueError('value must be > 0')


class NonBlank(Validated):

    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cammpt be empty or blank')
        else:
            return value


class LineItem:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

import collections

if __name__ == '__main__':
    item = LineItem('smallfat', 20, 5)
    print(item.subtotal())
    # item.weight = 15
    # print(item.subtotal())
    # print(vars(item))
    # item.weight = -2

    # print(item.subtotal())
    # d = Data(1, 2, 3)
    # print(d)
    # s = Student(20)
    # print(s.age)
    print(item.subtotal)
