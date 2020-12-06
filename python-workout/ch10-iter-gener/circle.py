class CircleIterator():

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0
    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value


class Circle():

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleIterator(self.data, self.max_times)


# Book's alternate solution
class Circle2():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
    def __iter__(self):
        n = len(self.data)
        return (self.data[x % n] for x in range(self.max_times))

c = Circle2('abc', 5)
print(list(c))

c1 = Circle('abcdefghij', 25)
print(list(c1))
