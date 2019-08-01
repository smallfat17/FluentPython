from collections import abc
from day16.Sentence_V1 import Sentence

class SentenceIterator(abc.Iterator):
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

def NewIter(self):
    return SentenceIterator(self.words)

if __name__ == '__main__':
    Sentence.__iter__ = NewIter
    s = Sentence('aaa  aas ss ')
    it = iter(s)
    print(next(it))
    print(next(it))
    print(next(it))
    # print(next(it))

