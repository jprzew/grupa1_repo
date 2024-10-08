try:
    number = int(input('Enter a natural number: '))
except ValueError:
    print('You must enter a natural number')
    exit(1)

if number % 2 == 0:
    print('Even number')
else:
    print('Odd number')
