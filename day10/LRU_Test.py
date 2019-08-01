import functools
import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        t1 = time.perf_counter() - t0
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[%0.8f] %s(%s) -> %r' % (t1, name, arg_str, result))
        return result
    return clocked

@functools.lru_cache()
@clock
def fabonacci(n):
    return n if n < 2 else fabonacci(n-2) + fabonacci(n-1)

if __name__ == '__main__':
    print(fabonacci(300)) #[0.00416574] fabonacci(10) -> 55
                         #[0.00009223] fabonacci(10) -> 55  LRU