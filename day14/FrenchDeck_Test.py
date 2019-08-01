import random
from collections import namedtuple
from collections.abc import MutableSequence


Card = namedtuple('Card', 'rank suit')

class FrenchDeck(MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, index: int, object: Card):
        self._cards.insert(index, object)

if __name__ == '__main__':
    french = FrenchDeck()
    print(french[2:5])
    # FrenchDeck.__setitem__ = set_deck
    random.shuffle(french)
    print(french[:5])

    french.append(Card('1', '2'))
    print(french[-5:])
    french.remove(Card('1', '2'))
    print(french[-5:])

    del french[-1]
    print(french[-5:])
    
