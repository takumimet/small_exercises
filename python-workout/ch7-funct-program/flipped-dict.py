
example = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

def flip_dict(dictio):
    return {dictio[key]: key for key in dictio}

# Book's solution
def flipped_dict(a_dict):
    return {value: key
            for key, value in a_dict.items()}

print(example.items())
print(flip_dict(example))
print(flipped_dict(example))

# Given a string containing several (space-separated) words, create a dict in which
# the keys are the words, and the values are the number of vowels in each word.

def vowel_len(word):
    output = 0
    for letter in word:
        if letter in 'aeiou':
            output += 1
    return output

def word_dict(string):
    return {word: vowel_len(word) for word in string.split()}

print(word_dict('This is only the beginning'))

                
