import os

class All_Lines():

    def __init__(self, dirname):
        self.dirname = dirname
        self.files = list(os.walk(self.dirname))[0][2]
        self.index = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration
        try:
            value = os.path.join(self.dirname, self.files[self.index])
            self.index += 1
            return [line.strip() for line in open(value)]
        except OSError:
            self.index += 1
            pass


for items in os.walk('all-files'):
    print(items)

lines = All_Lines('all-files')

# for line in lines:
#     print(line)

# Book's solution JAJAJAJAJAJAJA
def all_lines(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path,
                                        filename)
        try:
            for line in open(full_filename):
                yield line
        except OSError:
            pass

# for line in all_lines('./all-files'):
#     print(line)
