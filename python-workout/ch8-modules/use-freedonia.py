from freedonia import calculate_tax

print(calculate_tax(500, 'Harpo', 45))

tax_at_12noon = calculate_tax(100, 'Harpo', 12)
tax_at_9pm = calculate_tax(100, 'Harpo', 45)

print(f'You owe a total of: {tax_at_12noon}')
print(f'You owe a total of: {tax_at_9pm}')
