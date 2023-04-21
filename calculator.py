# create a class calculator.
# to run this, in the terminal $ python calculator.py. you should have python installed.
class Calculator:
    # initialize result to 0
    def __init__(self):
        self.result = 0

    # define a method for addition
    def add(self, num1, num2):
        self.result = num1 + num2

    # define a method for subtraction
    def subtract(self, num1, num2):
        self.result = num1 - num2

    # define a method for multiplication
    def multiply(self, num1, num2):
        self.result = num1 * num2

    # define a method for division
    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        self.result = num1 / num2

    # define a method to clear
    def clear(self):
        self.result = 0


# have prompts in the command-line interface for running this script
if __name__ == '__main__':
    calculator = Calculator()
    while True:
        print("Current result:", calculator.result)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.add(num1, num2)

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.subtract(num1, num2)

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.multiply(num1, num2)

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.divide(num1, num2)

        elif choice == '5':
            calculator.clear()

        elif choice == '6':
            break

        else:
            print("Invalid choice")
