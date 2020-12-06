import string

def gematria():
    return {char: index for char, index in enumerate(string.ascii_lowercase, 1)}

print(gematria())

def dict_forcer(filename):
    return {key: value for key, value in [line.strip().split('=') for line in open('config.txt')]}

print(dict_forcer('config.txt'))

def dict_forcer2(filename):
    return {key: int(value) for key, value in [line.strip().split('=') for line in open('config.txt')] if value.isnumeric()}

print(dict_forcer2('config.txt'))    
