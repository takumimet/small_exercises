import time
import os

def elapsed(iterable):
    last_time = time.perf_counter()
    for item in iterable:
        yield item, (time.perf_counter() - last_time)


# for i in elapsed('asdfgh'):
#     print(i)
#     time.sleep(3)

def elapsed_since2(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time
                                or current_time)
        last_time = time.perf_counter()
        yield (delta, item)
# for t in elapsed_since2('abcd'):
#     print(t)
#     time.sleep(2)

def file_using_timing(dir):
    files = list(os.walk(dir))[0][2]
    for file in files:
        direct = list(os.stat(os.path.join(dir, file)))
        yield (file, 'Date Created: {0[9]}, Date Modified: {0[8]}, Date Accessed: {0[7]}'.format(direct))

for t in file_using_timing('./all-files'):
    print(t)

def func_gen(iterable, func):
    return (item for item in iterable if func(item))

for i in func_gen(['1', 'a', 'b', '5', 'v', '7', '9'], str.isalpha):
    print(i)
