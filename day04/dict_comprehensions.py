from collections import defaultdict
data = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country: code for code, country in data}
print(country_code)

class MyDefaultDict(dict):
    def __missing__(self, key):
        print('missing..')
        return None

d = MyDefaultDict([('one', 1), ('four', 4)])
d['one'] = 1
# d.__getitem__('ok')

print(d)


d = {'a': [2]}
d.setdefault('a', []).append(1)
print(d)

def One():
    return 0

from collections import defaultdict

dd = defaultdict(One)
dd['one'] = dd['one'] + 1
print(dd)