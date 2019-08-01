import time
import asyncio

def func1(n):
    while True:
        for i in range(10):
            a = yield from fabnacci(n)
            print(a)
            # print('i: ',i)

def fabnacci(n):
    a, b = 1, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1
    return 'done'

@asyncio.coroutine
def smart_fb(n):
    a,  b = 1, 1
    while n > 0:
        yield from asyncio.sleep(2)
        print('smart: ',a)
        a, b = b, a+b
        n -= 1

@asyncio.coroutine
def stupid_fb(n):
    a,  b = 1, 1
    while n > 0:
        yield from asyncio.sleep(2)
        print('stupid: ', a)
        a, b = b, a+b


if __name__ == '__main__':
    # g = func1(10)
    # for i in range(20):
    #     print(next(g))

    loop = asyncio.get_event_loop()
    tasks = [smart_fb(10),stupid_fb(10)]
    loop.run_until_complete(asyncio.wait(tasks))



