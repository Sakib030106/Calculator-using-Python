# This is a simple calculator using Python.

# Introduction:
name = input('Hi! Welcome to this calculator. Please enter your name: ')
c = name.title()
print('Welcome,', c)

# Functions:
def add(x, y):    # This function adds two numbers.
    return x + y
def sub(x, y):    # This function subtract two numbers.
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

print('Select Operation: ')
print('Press 1 to add. ')
print('Press 2 to subtract. ')
print('Press 3 to multiply. ')
print('Press 4 to divide. ')
print('Press 0 to exit. ')

# Engine:
while True:
    try:
        # Take user input.
        choice = input('Enter choice (1/2/3/4/0): ')

        if choice in ('1', '2', '3', '4'):
            num1 = input('Enter first number: ')
            num2 = input('Enter second number: ')
            num1 = float(num1)
            num2 = float(num2)

            if choice == '1':
                print(num1, '+', num2, '=', add(num1, num2))
            elif choice == '2':
                print(num1, '-', num2, '=', sub(num1, num2))
            elif choice == '3':
                print(num1, '*', num2, '=', mul(num1, num2))
            elif choice == '4':
                print(num1, '/', num2, '=', div(num1, num2))
            break
        elif choice == '0':
            break
        else:
            print('Invalid Input. Try again. ')
    except ValueError:
        print('Invalid Input. Try again. ')
        continue

# End:
end = input('Thank you for using this program. See you soon! ')