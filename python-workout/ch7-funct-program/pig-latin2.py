""" If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
 If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay.”"""

def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

def piglatin2(filename):
    with open(filename) as file:
        return ' '.join(plword(word) for line in file for word in line.split())


print(piglatin2('wcfile.txt'))

# Write a new function, funcfile, that will take two arguments—a filename and a
# function. The output from the function should be a string, the result of invok-
# ing the function on each word in the text file.
def funcfile(filename, func):
    with open(filename) as file:
        return ' '.join(func(word) for line in file for word in line.split())

print(funcfile('wcfile.txt', plword))

# Use a nested list comprehension to transform a list of dicts into a list of two element (name-value) tuples
def dict_to_tuple(lst):
    return [(key, dictio[key]) for dictio in lst for key in dictio]

print(dict_to_tuple([{'A': 1, 'B': 2}, {'C': 3, 'D': 4, 'A': 1}]))
