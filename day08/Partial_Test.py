from functools import partial
from operator import mul

print(mul(4, 5)) #20
partial_mul = partial(mul, 4)
print(partial_mul(5))  #20

from unicodedata import normalize

s1 = 'café'
s2 ='cafe\u0301'
print(s1, s2)
print(s1 == s2)

nfc = partial(normalize, 'NFC')
print(nfc(s1), nfc(s2))
print(nfc(s1) == nfc(s2)) #True

def fn(a, b=3, *args, cls='c', **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    print('cls: %s' % cls)
    for key, value in kwargs.items():
        print(key, value)

# fn('a', 'b', 'c', 'd', e='e', cls='cc', f='f')
fn_partial = partial(fn, 'a_p','bp', 'cc', cls='ccc',ff='ff')
fn_partial('ee','ff')
