class A:

    prop = 'xixixi'

    def __init__(self, data):
        self.data = data

    @property
    def prop(self):
        print('property')
        return 'property of prop'

if __name__ == '__main__':
    a = A('smallfat')
    print(a.prop)