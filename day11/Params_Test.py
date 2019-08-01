def func(a, b):
    a += b
    return a

def default_test(a = []):
    a.append(1)
    return a

if __name__ == '__main__':
    a,b = 1, 2
    print(func(a, b))
    print(a) #1
    a, b = [1, 2], [3, 4]
    print(func(a, b))
    print(a)  #[1, 2, 3, 4]
    a, b = (1 ,2), (3, 4)
    print(func(a, b))
    print(a) #(1, 2)

    a = [1, 2]
    print(default_test(a))
    print('default:',default_test())
    print('default:',default_test()) #default: [1, 1] 修改的还是默认列表