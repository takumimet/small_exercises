class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops(flavors):
    output = [Scoop(item) for item in flavors]

    for n, item in enumerate(output):
        print(n, item.flavor)

    return output

# scoops = create_scoops(['chocolate', 'vanilla', 'persimmon'])

class Beverages:
    def __init__(self, name, temp=75):
        self.name = name
        self.temp = temp
    def __repr__(self):
        return f'{self.name}, {self.temp}'

drinks = [Beverages(item) for item in ['Coke', 'Horchata', 'Café']]

for items in drinks:
    print(items)


perreo = Beverages('Michelada', 5)

print(perreo)
