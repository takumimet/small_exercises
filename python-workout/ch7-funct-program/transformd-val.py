def transform_values(func, iter):
    return {key: func(value) for key, value in iter.items()}

d = {'a':1, 'b':2, 'c':3}
print(transform_values(lambda x: x*x, d))

# Expand the transform_values exercise, taking two function arguments, rather
# than just one. The first function argument will work as before, being applied to
# the value and producing output. The second function argument takes two arguments,
# a key and a value, and determines whether there will be any output at all
def transform_values(func1, func2, iter):
    return {key: func1(value) for key, value in iter.items() if func2(key, value)}
