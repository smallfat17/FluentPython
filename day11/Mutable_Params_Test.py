class Bus:
    def __init__(self, passengers = None):
        if passengers == None:
            self.passengers = []
        else:
            #self.passengers = passengers
            self.passengers = passengers[:]

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

if __name__ == '__main__':
    student_list = ['jack', 'tom', 'bob', 'lilith']
    bus = Bus(student_list)
    print(bus.passengers)
    bus.drop('jack')
    bus.drop('tom')
    print(bus.passengers) #['bob', 'lilith']
    print(student_list) #['bob', 'lilith']  引用
                        #  #['jack', 'tom', 'bob', 'lilith'] 复本