import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentense(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (x for x in self.words)

class A:
    def __iter__(self):
        pass


if __name__ == '__main__':
    # s = Sentence('"The time has come," the Walrus said,')
    # print(s)
    # for world in s:
    #     print(world)
    #
    # print(list(s))
    # iter(s)
    print(issubclass(A, abc.Iterable))
    print(issubclass(Sentence, abc.Iterable))
    print()
    s = Sentence('"The time has come," the Walrus said,')

    print(next(iter(s)))

    it = iter(range(10))
    print(next(it))
    iter()