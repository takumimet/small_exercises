def calculate_tax(amount, province, hour):
    place = {'Chico': 0.5 , 'Groucho': 0.7,
             'Harpo': 0.5,  'Zeppo': 0.4}
    tax = hour / 24

    return amount + (amount * (place[province] * tax))

print(calculate_tax(500, 'Harpo', 12))
