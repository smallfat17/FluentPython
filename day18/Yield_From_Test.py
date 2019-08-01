from collections import abc

def flatten(items, ignore_type=(str, int)):
    for item in items:
        if isinstance(item, abc.Iterable) and not type(item) in ignore_type:
            yield from flatten(item)
        else:
            yield item

def averager():
    total = 0
    count = 0
    # result = None
    while True:
        value = yield
        if value is None:
            break
        total += value
        count += 1
    return total / count

def grouper(results, key):
    while True:
        results[key] = yield from averager()
        print('{} done'.format(key))

def main(data):
    results = {}
    for key, values in data.items():
        g = grouper(results, key)
        g.send(None)
        for value in values:
            g.send(value)

        g.send(None)
    print(results)


if __name__ == '__main__':
    # print(isinstance([1, 2, 3], abc.Iterable))
    a = [1, 2, [3, 4, 5, [6, 7], [8, 9]], [10], 11]

    print(list(flatten(a)))
    data = {
        'girls;kg':
            [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'girls;m':
            [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
        'boys;kg':
            [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys;m':
            [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
    }
    main(data)

