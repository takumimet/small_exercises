
# Didn't understand :( this is book's solution
def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(
                f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()
        print('Not a valid option')

def func_a():
    return "A"
def func_b():
    return "B"

def a_sert():
    assert menu(a=func_a) == 'A'

def b_sert():
    assert menu(b=func_b) == 'B'

#
# return_value = menu(a=func_a, b=func_b)
# print(f'Result is {return_value}')

if __name__ == '__main__':
    a_sert()
    b_sert()
