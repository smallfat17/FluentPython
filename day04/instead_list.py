import array
import random

# floats = array.array('d', (random.random() for _ in range(10**7)))
#
# fp = open('floats.bn', 'wb')
# floats.tofile(fp)
# fp.close()
# print(floats[-1])
# print(floats[:10])
#
# floats2 = array.array('d')
# fp = open('floats.bn', 'rb')
# floats2.fromfile(fp, 9)
# fp.close()
# print(floats2[-1])
# print(floats2[:10])
# print(floats == floats2)

import pickle
class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender =gender

    def speak(self):
        print(self.name,' says hello')

    def __repr__(self):
        return 'name: %r gender: %r'  %(self.name, self.gender)

    def __eq__(self, other):
        return self.name == other.name and self.gender == other.gender



fp = open('stu.pickle', 'wb')
stu = Student('jack', 'M')
pickle.dump(stu, fp)

fp = open('stu.pickle', 'rb')
stu2 = pickle.load(fp)
stu2.speak()
print(stu2)
print(stu == stu2)