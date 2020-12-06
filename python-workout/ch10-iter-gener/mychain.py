def my_chain(*args):
    for arg in args:
        # if isinstance(arg, dict):
        #     for item in arg.items():
        #         yield item[1]
        #     for item in arg.items():
        #         yield item[0]

        for item in arg:
            yield item


def my_chain2(*args):
    return (item for arg in args for item in arg)


# for one_item in my_chain2('abc', [1,2,3], {'a':1, 'b':2}):
#     print(one_item)


def my_zip(*args):
    for index in range(len(args), 2):
        for item in arg[index]:
            for value in arg[index + 1]:
                yield (item, value)

for i, n in my_zip('abc', [10, 20, 30]):
    print(i, n)
