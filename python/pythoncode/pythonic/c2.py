class BoolCollection:
    def __init__(self):
        self.data = ['1', '2', '3']
        self.cur = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r


books = BoolCollection()
for book in books:
    print(book)