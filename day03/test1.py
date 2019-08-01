#切片, list的+、*、+=、*= ,list.sort、sorted

import random
if __name__ == '__main__':
    #切片
    l = list(range(10))
    l[2:5] = (100, 200) #一定是可迭代类型
    print(l) #[0, 1, 100, 200, 5, 6, 7, 8, 9]

    l[2:5] = {55: '1', 66: '2'} #
    print(l) #[0, 1, 55, 66, 6, 7, 8, 9]

    del l[2:5]
    print(l) #[0, 1, 7, 8, 9]

    #+ * += *=
    #列表的+和*
    a = [[]] * 3  #复制列表的引用
    print(a)
    print([id(ele) for ele in a])  #[1969315603144, 1969315603144, 1969315603144]
    a[0].append('1')
    print(a)  #[['1'], ['1'], ['1']]

    b = [[]*3 for i in range(3)]  #新建内存空间
    print(b)
    print([id(ele) for ele in b]) #[1969316490824, 1969316490760, 1969316490696]
    b[0].append(1)
    print(b)  #[[1], [], []]

    t = (1, 2, [30, 40])
    # t[2] += [50, 60]
    print(t)  #TypeError,但是t[2]的值已经改变

    #sorted list.sort
    def gen():
        for i in range(20):
            yield random.randint(0, 50)


    sort_gen_list = sorted(gen())  # [1, 1, 2, 3, 4, 5, 5, 7, 18, 20, 22, 25, 28, 28, 32, 36, 36, 37, 46, 48]
    print(sort_gen_list)
