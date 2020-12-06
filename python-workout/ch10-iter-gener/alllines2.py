import os

def all_lines(path):
    for num, filename in enumerate(os.listdir(path)):
        full_filename = os.path.join(path,filename)
        try:
            for nl, line in enumerate(open(full_filename)):
                yield (filename, num, nl, line)
        except OSError:
            pass

# for line in all_lines('all-files'):
#     print(line)

# Modify all_lines such that it takes two arguments—a directory name, and a
# string. Only those lines containing the string (i.e., for which you can say s in
# line) should be returned. If you know how to work with regular expressions
# and Python’s re module, then you could even make the match conditional on a
# regular expression.

def all_lines2(path):
    while True:
        number = 0
        try:
            index = number
            file_list = os.listdir(path)
            length = len(file_list)
            for line in open(file_list[index % length]):
                number += 1
                yield line[index % len(open(file_list[index % length]))]
        except OSError:
            number += 1
            pass

# for line in all_lines2('all-files'):
#     print(line)
