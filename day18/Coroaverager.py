import asyncio
import functools

class DemoException(Exception):
    pass


def coroutine(func):
    @functools.wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.send(None)
        return gen
    return primer


@coroutine
def averager():
    total = 0
    count = 0
    average = 0
    while True:
        try:
            term = yield average
        except TypeError:
            yield 'hahahaha'
        except GeneratorExit:
            print('genertor exit...')
            break
        total += term
        count += 1
        print(count)
        average = total / count
    print('byebye')

def demo_exc_handing():
    print('demo start...')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('Demo Exception')
            else:
                print('data receive: {}'.format(x))
    finally:
        return 'value: smallfat'
    # raise RuntimeError('this should not be happened')

if __name__ == '__main__':
    # avg = averager()
    # # avg.send(Ellipsis)
    # # avg.send(None) #使用了装饰器
    # print(avg.send(5))
    # print(avg.send(4))
    # print(avg.send(3))
    # # avg.close()
    # b = avg.throw(TypeError('???'))
    # print(b)
    # print(avg.send(3))
    #
    # avg.close()
    dg = demo_exc_handing()
    dg.send(None)
    dg.send('hello')
    dg.send('hello')
    dg.send('hello')
    dg.throw(DemoException)
    try:
        dg.throw(StopIteration)
    except StopIteration as exc:
        print(exc.value)


