class MyEnumerate():

    def __init__(self, data, start_index=0):
        self.data = data
        self.index = start_index
        self.start = start_index
    def __iter__(self):
        return self

    def __next__(self):
        if (self.index - self.start) >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

list1 = MyEnumerate(['a', 'b', 'c', 'd'])

for n, i in list1:
    print(n, i)

for n, i in list1:
    print(n, i)
