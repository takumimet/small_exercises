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

            # If you write a class attribute if you plan to
            # use it, you have to call it as such (see Bowl.max_scoop)
            if len(self.scoops) > Bowl.max_scoop:
                raise EOFError('Can\'t have more than 3')

    def __str__(self):
        # Very interesting
        return '\n'.join(s.flavor for s in self.scoops)

chocolate = Scoop('chocolate')

vainilla = Scoop('vainilla')

persimmon = Scoop('persimmon')

fresa = Scoop('fresa')

test = Bowl()

test.add_scoops(chocolate, vainilla)

print(test)

test.add_scoops(persimmon)

print(test)

test.add_scoops(fresa)
