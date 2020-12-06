class LogFile:
    def __init__(self, filename):
        self.filename = filename
        self.open = open(filename, 'a')

experiment = LogFile('test1.txt')

with experiment.open as file:
    file.write('What up?')
