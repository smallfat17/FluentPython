with open('test1.txt', 'w') as f:
    f.write('hello 世界'.encode('latin1', errors='replace')) #UnicodeEncodeError: 'latin-1' codec can't encode characters in position 6-7: ordinal not in range(256)
    # f.write('hello 世界'.encode('utf8'))

s = 'hello 世界'
print(s.encode(encoding='iso8859_1',errors='ignore')) #b'hello '
print(s.encode(encoding='iso8859_1',errors='replace')) #b'hello ??'
print(s.encode(encoding='iso8859_1',errors='xmlcharrefreplace')) #b'hello &#19990;&#30028;'


octests = 'Montréa1'.encode('latin_1') # 使用latin编码的Montréa1
print(octests.decode('cp1252')) #Montréa1
print(octests.decode('iso8859_7')) #Montrιa1
print(octests.decode('koi8_r')) #MontrИa1
# print(octests.decode('utf-8')) #UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
print(octests.decode('utf-8', errors='ignore'))  #Montra1 被utf8的替换字符代替

你 = 'o'
print(你)





