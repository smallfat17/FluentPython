from time import strftime, sleep
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M:%S] '), end='')
    print(*args)

def loiter(n):
    msg = '{}loiter doing noting for {}s'
    display(msg.format('\t' * n, n, n))
    # if n> 2:
    #     sleep(2)
    # else:
    sleep(n)
    msg = '{}loiter ({}): done'
    display(msg.format('\t' * n,  n, n))
    return n * 10

def main():
    display('Script starting')
    executor = futures.ThreadPoolExecutor(3)
    results = executor.map(loiter, range(5))
    display('results: ', results)
    display('Wating for individual results: ')
    for i, result in enumerate(results):
        display('result: {}: {}'.format(i, result))

if __name__ == '__main__':
    main()
