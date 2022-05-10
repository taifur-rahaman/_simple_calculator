
print(
'''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

print("Welcome to the Simple Calculator!\n")

def addition(operand_1, operand_2):
    return operand_1 + operand_2

def subtraction(operand_1, operand_2):
    return operand_1 - operand_2

def multiple(operand_1, operand_2):
    return operand_1 * operand_2

def divide(operand_1, operand_2):
    return operand_1 / operand_2

def calculation(operand_1, operand_2, operator):
    if operator == "+":
        result = addition(operand_1, operand_2)
        print(f"{operand_1} + {operand_2} = {result}")
    elif operator == "-":
        result = subtraction(operand_1, operand_2)
        print(f"{operand_1} - {operand_2} = {result}")
    elif operator == "*":
        result = multiple(operand_1, operand_2)
        print(f"{operand_1} * {operand_2} = {result}")
    elif operator == "/":
        result = divide(operand_1, operand_2)
        print(f"{operand_1} + {operand_2} = {result}")
    else:
        print("INVALID input")

    return result

operand_1 = float(input("What is the first number: "))
operator = input("Select operator:\n+\n-\n*\n/\nEnter your choice: ")
operand_2 = float(input("What is the second number: "))

while True:
    result = calculation(operand_1,operand_2, operator)

    choice = int(input(f"1. Continue calculating with {result}\n2. Start a new equation\n0. Quit\nEnter your choice: "))

    if choice == 1:
        operand_1 = result
        operator = input("Select operator:\n+\n-\n*\n/\nEnter your choice: ")
        operand_2 = float(input("What is the second number: "))
        continue
    elif choice == 2:
        operand_1 = float(input("What is the first number: "))
        operator = input("Select operator:\n+\n-\n*\n/\nEnter your choice: ")
        operand_2 = float(input("What is the second number: "))
        continue
    elif choice == 0:
        print("Thank you for using Our calculator!!")
        break