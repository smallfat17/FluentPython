class Student:
    def __init__(self, name, gender, lessons=None):
        self.name = name
        self.gender = gender
        self.lessons = lessons

    def __hash__(self):

        return super().__hash__()

    def __eq__(self, other):
        return self.lessons == other.lessons

if __name__ == '__main__':
    stu = Student('jack', 'M', ['english', 'math'])
    stu2 = Student('jack', 'F', ['english', 'math'])

    print(hash(stu))
    # stu.lessons.append('pe')
    
    print(stu==stu2)


