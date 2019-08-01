from types import MappingProxyType

d = {'a': 1, 'b': 2}
mpt_d = MappingProxyType(d)
print(mpt_d) #{'a': 1, 'b': 2}
# mpt_d['a'] = 3  #TypeError: 'mappingproxy' object does not support item assignment
d['a'] = 4
print(mpt_d) #{'a': 4, 'b': 2}
