def factorial(*numbers):
    output = 1
    for num in numbers:
        output = output * num
    return output

print(factorial(1, 2, 3, 4, 5, 6, 7, 8))        
