class Books():

    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width

class Shelf():

    def __init__(self):
        self.books = []
        self.maxwidth = 70 #cm
        self.usedwidth = 0

    def add_book(self, *items):

        for item in items:
            self.books.append(item)
            self.update_width()

            if self.usedwidth > self.maxwidth:
                raise Exception("Shelf can't add new item")

    def total_price(self):
        return sum(item.price for item in self.books)

    def update_width(self):
        self.usedwidth = sum(item.width for item in self.books)

    def __str__(self):
        return '\n'.join(f'{book.title}, {book.author}' for book in self.books)

    def has_book(self, book):
        if book in [item.title for item in self.books]:
            return True

        return False

bolaño = Books('Lluvia de Mierda', 'Roberto Bolaño', 25, 15)
piglia = Books('Plata Quemada', 'Ricardo Piglia', 15, 15)
neuman = Books('Hablar Solos', 'Andrés Neuman', 25, 20)
schweblin = Books('Kentukis', 'Samanta Schweblin', 20, 15)

upper_shelf = Shelf()
upper_shelf.add_book(bolaño, piglia)
print(upper_shelf.total_price())
print('wo neuman', upper_shelf.usedwidth)
upper_shelf.add_book(neuman)
print(upper_shelf.total_price())
print(upper_shelf.usedwidth)
upper_shelf.add_book(schweblin)
print(upper_shelf)
print(upper_shelf.has_book('El Tunel'))
