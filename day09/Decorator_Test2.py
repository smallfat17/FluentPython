import time
import functools

#输出函数运行时间的装饰器
def clock(func):
    @functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elasped = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elasped, name, arg_str, result))
        return result
    return clocked

@clock
def add(a, b):
    time.sleep(0.5)
    return a+b

if __name__ == '__main__':
    print('result',add(1, 2))
    print(add.__name__)  #add   因为functolls.wraps将add的属性赋值给了clocded

