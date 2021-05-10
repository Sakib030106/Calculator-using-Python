# This is a simple calculator using Python.

# Introuction:
name = input("Hi. This is a simple calculator. Please enter your name: ")
c = name.title()
print("Welcome,", c)

# Functions:


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Press 1 to add numbers. ")
print("Press 2 to subtract numbers. ")
print("Press 3 to multiply numbers. ")
print("Press 4 to divide numbers. ")
print("Press 0 to exit. ")

while True:
    try:
        choice = input("Please enter your operation(1/2/3/4/0): ")

        correction = choice.strip()

        if correction in ('1', '2', '3', '4'):
            num1 = input("Please enter your first number: ")
            num2 = input("Please enter your second number: ")
            num1 = float(num1)
            num2 = float(num2)

            if correction == '1':
                print(num1, '+', num2, '=', add(num1, num2))
            elif correction == '2':
                print(num1, '-', num2, '=', sub(num1, num2))
            elif correction == '3':
                print(num1, '*', num2, '=', multiply(num1, num2))
            elif correction == '4':
                print(num1, '/', num2, '=', divide(num1, num2))
        elif correction == '0':
            break
        else:
            print("Invalid input. Try again!")
    except ValueError:
        print("We only accept numbers. Try again.")

# End:
end = input("Thank you for using this program. See you soon! ")
