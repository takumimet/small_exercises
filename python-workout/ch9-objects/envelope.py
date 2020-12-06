class Envelope:

    rate = 10
    def __init__(self, weight, was_sent=False):
        self.weight = weight
        self.was_sent = was_sent
        self.postage = 0
        self.need_postage = self.rate * self.weight

    def add_postage(self, amount):
        self.postage += amount

    def postage_needed(self):
        print(f'Not enough postage.\nCurrent:{self.postage}\nNeeded:{self.need_postage}')

    def send(self):
        if self.postage >= self.need_postage:
            self.was_sent = True
        return postage_needed

class BigEnvelope(Envelope):

    rate = 15
    def __init__(self, weight, was_sent=False):
        super().__init__(weight, was_sent=False)

carta1 = Envelope(35)
carta1.postage_needed()
carta2 = BigEnvelope(35)
carta2.postage_needed()
