import struct

fmt = '<3s3sHH'
with open(r"test.gif", 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(struct.unpack(fmt, header)) #(b'GIF', b'89a', 320, 182) 类型、版本、宽度、高度

