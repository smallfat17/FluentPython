class Student:
    def __init__(self, name):
        self._name = name

    def __call__(self, *args, **kwargs):
        print(self._name)

s = Student('Jack')
print(callable(s))
s()


def my_decoration(fn):
    def wrapper():
        print('before')
        fn()
        print('after')
    return wrapper

@my_decoration
def test():
    print('test...')

test()