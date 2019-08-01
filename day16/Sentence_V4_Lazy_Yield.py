import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence (%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match

if __name__ == '__main__':
    s = Sentence('"This guy has no chill!", he said,')
    for word in s:
        print(word)
    # print(s)10