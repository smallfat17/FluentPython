import sys

class LookingGlass:
    def __init__(self, face):
        self.face = face

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return self.face

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('do not divide by zero')
            return True

if __name__ == '__main__':
    g = LookingGlass('smallfat')
    text = g.__enter__()
    print(text)
    print(text == 'smallfat')
    g.__exit__(None, None, None)
    print(text)

    with LookingGlass('smallfat') as s:
        print(s)
    print(s)

