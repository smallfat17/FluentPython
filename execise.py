import asyncio
from time import strftime

from functools import wraps
from time import perf_counter


#打印运行时间的装饰器
def perf_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = perf_counter()
        result = func(*args, **kwargs)
        print('perf: {:.10f}'.format(perf_counter() - t0))
        return result
    return wrapper


#日志装饰器
def logit(logfile='out2.log'):
    def logging_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_str = func.__name__ + ' was called'
            print(log_str)
            with open(logfile, 'a', encoding='utf8') as f:
                f.write(strftime('[%H:%M:%S]') + log_str + '\n')
            result = func(*args, **kwargs)
            print(func.__name__, ' was finished')
            return result
        return wrapper
    return logging_func


class log:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print(self._func.__name__, ' was called')
        result = self._func(*args, **kwargs)
        print('end..')
        return result


# @perf_time
@log
def test(time):
    return time





if __name__ == '__main__':
    for i in range(1000):
        a = test(i)
        print('time: ', a)
    print(type(test))

    # print(test.__name__)