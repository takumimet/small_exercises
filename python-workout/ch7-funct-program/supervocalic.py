def supervocalic(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return vowels & set(word) == vowels

def get_sv(filename):
    with open(filename) as file:
        return {word for line in file for word in line.split() if supervocalic(word)}

# print(get_sv('words.txt'))

# The book's solution works beacuse the operator '<'
# checks if the left side set is a SUBSET of the
# one in the right.
def get_sv2(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip()
        for word in open(filename)
        if vowels < set(word.lower())}

# print(get_sv2('words.txt'))

# Given a text file, what are the lengths of the different words? Return a set of dif-
# ferent word lengths in the file.
def set_lenght(filename):
    return {len(word) for line in open(filename) for word in line.split()}

print(set_lenght('words.txt'))

# Create a list whose elements are strings—the names of people in your family.
# Now use a set comprehension (and, better yet, a nested set comprehension) to
# find which letters are used in your family members’ names.
def name_letter(lst):
    return [set(letter for letter in word) for word in lst]

print(name_letter(['Marta', 'Marina', 'Alcides', 'Alonso']))
