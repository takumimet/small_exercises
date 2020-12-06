class Animal():
    legs_num = 4
    def __init__(self, color):
        self.color = color
        self.name = self.__class__.__name__

    def __str__(self):
        return f'{self.color} {self.name}, {self.legs_num} legs'

fernan = Animal('Brown')
print(fernan)

class Parrot(Animal):
    legs_num = 2


class Snake(Animal):
    legs_num = 2
    

class Wolf(Animal):
    legs_num = 2
    Animal.__init__

class Sheep(Animal):
    legs_num = 2
    Animal.__init__

parrot1 = Parrot('Blue')
snake1 = Snake('Green')
wolf1 = Wolf('Red')
sheep1 = Sheep('Black')

print(parrot1)
print(sheep1)
print(wolf1)
print(snake1)
