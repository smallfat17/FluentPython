from unicodedata import normalize
import unicodedata

u1 = 'café'
u2 = 'cafe\u0301'
u3 = 'cafe'

print(normalize('NFC', u1))
print(normalize('NFC', u2))
print(normalize('NFC', u1) == normalize('NFC', u2)) #True

print(normalize('NFD', u1))
print(normalize('NFD', u2))
print(normalize('NFD', u3))
print(normalize('NFD', u2) == normalize('NFD', u2)) #True
print(normalize('NFD', u1) == normalize('NFD', u3)) #False


s1 = 'hé ni yi qi'

def shave_marks(txt):
    '''
    删去变音符号
    :param txt:
    :return:
    '''
    norm_txt = normalize('NFD', s1)
    print(norm_txt)
    #过滤组合记号, NFD模式将变音符号拆分出来
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

print(shave_marks(s1))

s2 = normalize('NFD' ,'é')
print(s2[0], s2[1])
print(unicodedata.combining(s2[1]))

# import pyuca

open('hé.txt', 'w').write('nihao')