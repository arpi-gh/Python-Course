class MyIterable:
    def __init__(self, name):
        self.name = name
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        value = self.name[self.index]
        self.index += 1
        return value


it = MyIterable([1, 2, 3, 4])
for item in it:
    print(item)