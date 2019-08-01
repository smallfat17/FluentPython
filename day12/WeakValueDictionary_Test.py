import weakref

class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


if __name__ == '__main__':
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese

    print(sorted(stock)) #['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
    del catalog
    print(sorted(stock)) #['Parmesan']
    del cheese
    print(sorted(stock)) #[]
