import weakref

def func():
    print('Gone ....')

if __name__ == '__main__':
    s1 = {1, 2, 3}
    s2 = s1
    ender = weakref.finalize(s1, func)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'other' #Gone .... 对象被销毁，回调触发
    print(ender.alive) #False