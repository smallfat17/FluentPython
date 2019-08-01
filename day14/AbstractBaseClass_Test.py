import abc
import random

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        pass

    @abc.abstractmethod
    def pick(self):
        pass

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except:
                break
        self.load(items)
        return tuple(sorted(items))

class Fake(Tombola):
    def pick(self):
        pass

    #定义抽象类方法
    @classmethod
    @abc.abstractmethod
    def func(cls):
        pass

class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, iterable):
        self._items.extend(iterable)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty {.__name__!r}'.format(type(self)))

    def __call__(self, *args, **kwargs):
        return self.pick()

class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(self._balls)

    def __call__(self, *args, **kwargs):
        return self.pick()

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty {.__name__!r}'.format(type(self)))

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    #f = Fake() #TypeError: Can't instantiate abstract class Fake with abstract methods load
    # bingo = BingoCage([1, 2, 3])
    # print(bingo.pick())
    # print(bingo.pick())
    # print(bingo())

    # lottery = LotteryBlower([1, 2, 3, 4, 5, 6])
    # print(lottery.pick())
    # print(lottery.pick())
    # print(lottery.pick())
    # print(LotteryBlower.__mro__)

    tobolist = TomboList([1, 2, 3, 4, 5, 6, 7])
    print(tobolist.pick())
    print(tobolist.pick())
    print(tobolist.pick())
    print(isinstance(tobolist, Tombola))
    print(issubclass(TomboList, Tombola))
    print(TomboList.__mro__)


