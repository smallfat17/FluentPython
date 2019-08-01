class MySq:
    def __getitem__(self, item):
        return item

if __name__ == '__main__':
    sq = MySq()
    print(sq[10])
    print(sq[1:2])
    print(sq[1:2:2])
    print(sq[1:2:2, 2:3]) #(slice(1, 2, 2), slice(2, 3, None))