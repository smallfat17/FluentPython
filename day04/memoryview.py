import array

numbers = array.array('h', [1, 2, 3, 4])
memv = memoryview(numbers)
print(memv[0])

memv.tolist()
memv_oct = memv.cast('B')
memv_oct[5] = 4
print(numbers) #array('h', [1, 2, 1027, 4])

