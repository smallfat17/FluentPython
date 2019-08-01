import functools
import html
import numbers
from collections import abc

@functools.singledispatch
def htmlize(obj):
    # pass
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0}(0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    print(type(seq[0]))
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Student: %s' % self.name
if __name__ == '__main__':
    s1 = Student('jack')
    print(htmlize('abcd'))
    print(htmlize([1, 2, 3]))
    print(htmlize(['alpha',1, 1, ('dd', 'ee', s1)]))


