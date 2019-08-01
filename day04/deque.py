from collections import deque
import heapq




if __name__ == '__main__':
    #deque
    dq = deque(range(10), maxlen=5)  #maxlen属性限制队列长度
    print(dq)  #deque([5, 6, 7, 8, 9], maxlen=5)
    dq.rotate(2)  #类似传送带，正数向右滚动，负数向左边滚动
    print(dq) #deque([8, 9, 5, 6, 7], maxlen=5)
    dq.rotate(-2)
    print(dq) #deque([5, 6, 7, 8, 9], maxlen=5)
    dq.appendleft(1)#append的时候，如果len等于maxlen，则会“挤出”超过长度的部分
    print(dq) #deque([1, 5, 6, 7, 8], maxlen=5)
    dq.extendleft([-1, -2])
    print(dq) #deque([-2, -1, 1, 5, 6], maxlen=5)  #[-2, -1]逆序了

    print(-1 in dq)
    dq += [22]
    print(dq)
    print(dq*2)

    #heapq
    # h = heapq()
    lst = [1, 2, 3, 4, 5]
    data = heapq.heappop(lst)
    print(data)
    data = heapq.heappop(lst)
    print(data)
    data = heapq.heappop(lst)
    print(data)
    heapq.heappush(lst, 6)
    print(lst)


