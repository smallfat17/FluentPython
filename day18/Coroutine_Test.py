from inspect import getgeneratorstate
from multiprocessing import Semaphore

def simple_coroutine():
    x = yield
    getgeneratorstate()
    print(x)


if __name__ == '__main__':
    coro = simple_coroutine()
    print(getgeneratorstate(coro))
    print(coro.send(None))
    print(getgeneratorstate(coro))
    try:
        coro.send('hello')
    except StopIteration:
        print(getgeneratorstate(coro))

