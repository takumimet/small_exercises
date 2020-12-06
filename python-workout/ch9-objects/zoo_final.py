class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage():
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output

class Zoo():

    def __init__(self, *cages):
        self.cages = [*cages]
        pass

    def animals_by_color(self, *colors):
        return [animal for cage in self.cages for animal in cage.animals if animal.color in colors]

    def animals_by_legs(self, legs_num):
        return [animal for cage in self.cages for animal in cage.animals if animal.number_of_legs == legs_num]

    def number_of_legs(self):
        return sum(animal.number_of_legs for cage in self.cages for animal in cage.animals)

    def get_animals(self, **kwargs):
        if set(kwargs) == {'color', 'legs'}:
            return [animal for cage in self.cages for animal in cage.animals
                        if animal.color == kwargs.get('color')
                        if animal.number_of_legs == kwargs.get('legs')]
        elif 'color' in kwargs:
            return [animal for cage in self.cages for animal in cage.animals
                        if animal.color == kwargs.get('color')]
        elif 'legs' in kwargs:
            return [animal for cage in self.cages for animal in cage.animals
                        if animal.number_of_legs == kwargs.get('legs')]
        else:
            raise NameError("Only 'color and 'legs' are accepted")

    def __repr__(self):
        output = f'Zoo:'
        for cage in self.cages:
            output += f'\n\tCage {cage.id_number}:'
            output += '\n\t'.join('\t\t' + str(animal) for animal in cage.animals)
        return output

# wolf = Wolf('black')
# sheep = Sheep('white')
# snake = Snake('brown')
# parrot = Parrot('green')
# c1 = Cage(1)
# c1.add_animals(wolf, sheep)
# c2 = Cage(2)
# c2.add_animals(snake, parrot)
# print(c1)
# print(c2)
#
# z1 = Zoo(c1, c2)
# print(z1.number_of_legs())
# print(z1.animals_by_color('black'))
# print(z1.animals_by_legs(4))
# print(z1.get_animals(color='white'))
# print(z1)
