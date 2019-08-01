import collections

class mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

class MyDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

if __name__ == '__main__':
    d = MyDict(a=1)
    print(dir(d))
    print(d)
    d['b'] = 2
    print(d)    #使用了子类覆盖的__setitem__，其他均没有使用，使用MyDict能正常使用
    d.setdefault('c', 5)
    print(d)
    d.update(d='5')
    print(d)