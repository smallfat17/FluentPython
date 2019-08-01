from urllib.request import urlopen
from collections import abc
import warnings
import keyword
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON, encoding='utf8') as f:
        return json.load(f)


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            if item not in self.__data.keys():
                raise AttributeError('no such attribute name {!r}'.format(item))
            return FrozenJSON.build(self.__data[item])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == '__main__':
    feed = load()
    print(feed['Schedule'])

    fj = FrozenJSON(feed)
    print(fj.Schedule.speakers[-1].items())
    print(fj.Schedule.conferences)
    print(keyword.kwlist)

    fj2 = FrozenJSON({'class': 1, 'True': 2})
    print(fj2.class_)
    # fj.ss
