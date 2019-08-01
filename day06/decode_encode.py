s = 'abc'
b = s.encode('utf8')
print(b)  #b'abc'
print(type(b)) #<class 'bytes'>

s_b = b.decode('utf8')
print(s_b) #abc
print(type(s_b)) #<class 'str'>

