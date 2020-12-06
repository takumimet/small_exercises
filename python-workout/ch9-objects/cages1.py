class Animal():
    def __init__(self, color, legs_num, space_needs):
        self.legs_num = legs_num
        self.color = color
        self.name = self.__class__.__name__
        self.space_needs = space_needs
    def __str__(self):
        return f'{self.color} {self.name}, {self.legs_num} legs'

fernan = Animal('Brown', 2, 7)
print(fernan)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2, 50)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0, 10)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4, 30)

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4, 28)

class Cage:
    partners = {Sheep: [Sheep, Wolf], Wolf: [Wolf, Sheep],
                Parrot: [Parrot, Snake], Snake: [Snake, Parrot]}
    size = 100
    def __init__(self, id):
        self.id = id
        self.see_animals = []
        self.used_space = 0
        self.name = self.__class__.__name__
    def add_animals(self, *animals):
        for animal in animals:
            self.see_animals.append(animal)
            self.used_space += animal.space_needs

            if self.used_space > self.size:
                raise ValueError('Not enough space for another animal')
            # if self.see_animals:
            #     if animal.name not in self.partners[self.see_animals[0]]:
            #         raise ValueError('Pair intended not allowed')

    def __repr__(self):
        return f'{self.name} {self.id}: {[animal.name for animal in self.see_animals]}'

    # Book's solution
    # def __repr__(self):
    #     output = f'Cage {self.id}:\n'
    #     output += '\n'.join('\t' + str(animal)
    #             for animal in self.see_animals)
    #     return output

class BigCage(Cage):
    size = 1_000_000


parrot1 = Parrot('Blue')
snake1 = Snake('Green')
wolf1 = Wolf('Red')
sheep1 = Sheep('Black')

c1 = Cage(1)
c1.add_animals(parrot1, snake1) #, wolf1, sheep1)
print(c1)
bc1 = BigCage(1)
bc1.add_animals(parrot1, snake1, wolf1, sheep1)
print(bc1)
