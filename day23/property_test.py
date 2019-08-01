class Game:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return 'name: {} price: {}'.format(self.name, self.price)


    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.deleter
    # def name(self):
    #     text = 'GAME {} DELETED'
    #     print(text)
    #     del self
    #     return 'G'

if __name__ == '__main__':
    g = Game('1', 2)
    print(g)
    print(getattr(g, 'name'))
    # del g.name
    # print(getattr(g, 'name'))
    g.__dict__['value'] = 'smallfat'
    print(g.value)
    print(vars(g))
    print(help(g.__getattribute__))

