import operator as op

# The important thing about this exercise is that
# we can pass functions as data (see dict) in Python
def calc(strg):
    operations = {'+': op.add, '-': op.sub, 'x': op.mul,
                    '/': op.truediv, '^': op.pow, '%': op.mod}

    ope, first, second = strg.split()
    first = int(first)
    second = int(second)

    return operations[ope](first, second)


print(calc('+ 1 3'))

def rec_calc(strg):
    operations = {'+': op.add, '-': op.sub, 'x': op.mul,
                    '/': op.truediv, '^': op.pow, '%': op.mod}

    ope, first, *others = strg.split()
    output = int(first)
    rest = [int(n) for n in others]
    for num in rest:
        output = operations[ope](output, num)

    return output

print(rec_calc('+ 1 3 5 13'))
