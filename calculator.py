# Define our function
def main():
    operation = input('''
Please type in the math operation you would like to complete:
"Add" for addition
"Subtract" for subtraction
"Multiply" for multiplication
"Divide" for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == 'Add' or 'add' or '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == 'Subtract' or 'subtract' or '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == 'Multiply' or 'multiply' or '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == 'Divide' or 'divide' or '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('PUT A VALID NUMBER YOU FOOL!')

# Call calculate() outside of the function
main()