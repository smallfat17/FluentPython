import contextlib
import sys

@contextlib.contextmanager
def func():
    print('enter')
    yield 'hello'
    print('exit')

@contextlib.contextmanager
def lookglass():
    origin_write = sys.stdout.write
    def reverse_write(text):
       return origin_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'smallfat'
    sys.stdout.write = origin_write

@contextlib.contextmanager
def looking_glass():
    origin_write = sys.stdout.write

    def reverse_write(text):
        return origin_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'smallfat'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by Zero'
    finally:
        sys.stdout.write = origin_write
        if msg:
            print(msg)



if __name__ == '__main__':
    with lookglass() as f:
        print(f)
        print('ok')
        print('what?')

    print('smallfat')


    with looking_glass() as l:
        print(l)
        2/0
        print('ok')
        print('ok')


