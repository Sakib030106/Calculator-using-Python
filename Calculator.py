# This is a simple calculator using Python.

# Introduction:
name = input('Hi! This is a simple calculator. Please enter your name: ')
c = name.title()
print('Welcome', c)

# Functions:
def add(x, y):     # This function will add two numbers.
    return x + y
def sub(x, y):     # This function will subtract two numbers.
    return x - y
def mul(x, y):     # This function will multiply two numbers.
    return x * y
def div(x, y):     # This function will divide two numbers.
    return x / y

# Help:
print('Select Operation: ')
print('Enter 1 to add. ')
print('Enter 2 to subtract. ')
print('Enter 3 to multiply. ')
print('Enter 4 to divide. ')
print('Enter 0 to exit. ')

# Engine:
while True:
    try:
        choice = input('Please enter your choice(1/2/3/4/0): ')

        if choice in ('1', '2', '3', '4'):
            num1 = input('Please enter your first number: ')
            num2 = input('Please enter your second number: ')
            num1 = float(num1)
            num2 = float(num2)

            if (choice == '1'):
                print(num1, '+', num2, '=', add(num1, num2))
            elif (choice == '2'):
                print(num1, '-', num2, '=', sub(num1, num2))
            elif (choice == '3'):
                print(num1, '*', num2, '=', mul(num1, num2))
            elif (choice == '4'):
                print(num1, '/', num2, '=', div(num1, num2))
        elif (choice == '0'):
            break
        else:
            print('Invalid input. Please try again. ')
    except ValueError:
        print('Invalid input. Please try again. ')

# End:
end = input('Thank you for using this program. See you again! ')