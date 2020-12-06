class Animal():
    def __init__(self, color, legs_num):
        self.legs_num = legs_num
        self.color = color
        self.name = self.__class__.__name__

    def __str__(self):
        return f'{self.color} {self.name}, {self.legs_num} legs'

fernan = Animal('Brown', 2)
print(fernan)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

parrot1 = Parrot('Blue')
snake1 = Snake('Green')
wolf1 = Wolf('Red')
sheep1 = Sheep('Black')

print(parrot1)
print(sheep1)
print(wolf1)
print(snake1)
