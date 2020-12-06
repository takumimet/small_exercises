class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoop = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *scoop_flavors):
        # max_scoop = 3
        for items in scoop_flavors:
            self.scoops.append(items)

            # Easiest way to change it is to change
            # Bowl.max_scoop to self.max_scoop 
            if len(self.scoops) > self.max_scoop:
                raise EOFError('Can\'t have more than 3')

    def __str__(self):
        # Very interesting
        return '\n'.join(s.flavor for s in self.scoops)

class BigBowl(Bowl):

    max_scoop = 5
    def __init__(self):
        super().__init__()

chocolate = Scoop('chocolate')
vainilla = Scoop('vainilla')
persimmon = Scoop('persimmon')
fresa = Scoop('fresa')
galleta = Scoop('galleta')

test = BigBowl()
test.add_scoops(chocolate, vainilla, persimmon, fresa, galleta)

print(test)
