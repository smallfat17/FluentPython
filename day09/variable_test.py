
b = 6
def f1(a):
    print(a)
    print(b) #UnboundLocalError: local variable 'b' referenced before assignment
    b = 10

def f2(a):
    global b
    print(a)
    print(b)
    b = 7
if __name__ == '__main__':
    # f1(3)
    f2(3)
    print(b)
    import dis
    print(dis.dis(f2))