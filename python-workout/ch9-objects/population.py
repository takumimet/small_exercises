import sys, os
from itertools import count

class Popul:

    population = 0
    # _ids = count(0)
    def __init__(self):
        Popul.population += 1 # next(self._ids)

    def __del__(self):
        Popul.population -= 1

class Person(Popul):

    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age


p1 = Person('Menganito', 23)
p2 = Person('Fulana', 14)
p3 = Person('Pedro', 67)
p4 = Person('Sutanito', 29)
p5 = Person('Solútor', 27)

print(Person.population)
print(p1.population)
print(p5.population)
del(p1)
print(Person.population)
del(p2)
print(Person.population)
