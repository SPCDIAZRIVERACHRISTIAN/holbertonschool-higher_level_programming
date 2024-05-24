class CountedIterator:
    def __init__(self, counter):
        self.counter = counter
        self.count = 0
        self.iterator = iter(counter)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration('CountedIterator: StopIteration')

    def get_count(self):
        return self.count
