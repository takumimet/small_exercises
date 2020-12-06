import random

def create_password_generator(characters):
    def create_password(length):
        output = ''.join(random.choices(characters, k=length))
        return output

    return create_password

alpha_password = create_password_generator('abcdef')
print(alpha_password(5))

def check_passwd(min_up=4, min_low=4, min_dig=2, min_punt=2):
    def password(passwd):
        upper = len([char for char in passwd if char.isupper()])
        lower = len([char for char in passwd if char.islower()])
        digit = len([char for char in passwd if char.isdigit()])
        punct = len([char for char in passwd if not char.isalnum()])
        print(upper, lower, digit, punct)
        if upper >= min_up and lower >= min_low and digit >= min_dig and punct >= min_punt:
            return True
        else:
            return False
    return password

check1 = check_passwd()
print(check1('GHJKbnmv56$&Gn5'))
