import weakref

class Student():
    weakset = weakref.WeakSet()
    def __init__(self, name):
        self.name = name
        self.weakset.add(self)

    def __repr__(self):
        return 'Student (%r)' % self.name

if __name__ == '__main__':
    s1 = Student('jack')
    s2 = Student('tom')
    print(list(Student.weakset)) #[Student ('tom'), Student ('jack')]
    del s1
    print(list(Student.weakset)) #[Student ('tom')]
    del s2
    print(list(Student.weakset)) #[]
