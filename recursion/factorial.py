def factorial(x):
    print(x)
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

number = 5

print(f'The factorial of {number} is {factorial(number)}')
