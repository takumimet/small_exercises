class Transaction:

    balance = 0
    def __init__(self, amount):
        self.amount = amount
        Transaction.balance += amount

deposit1 = Transaction(500)
print(Transaction.balance)
withdraw = Transaction(-90)
print(Transaction.balance)        
