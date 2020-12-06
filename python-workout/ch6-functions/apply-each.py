
def apply_to_each(func, iterable):
    output = []
    for item in iterable:
        output.append(func(item))
    return output

print(apply_to_each(len, ['tasa', 'caca', 'oscar de la renta', 'pedo']))

        
