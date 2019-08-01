
#装饰器

def decorate(func):
    print('running docorate')
    def inner():
        func()
        print('running inner')
    return inner

@decorate
def target():
    print('runing target().')

if __name__ == '__main__':
    print('running main')
    target()