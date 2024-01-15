def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def main():
    while True:
        print("\nOptions:")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'quit' to end the program")
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ('add', 'subtract', 'multiply', 'divide'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("Result: ", add(num1, num2))
            elif user_input == "subtract":
                print("Result: ", subtract(num1, num2))
            elif user_input == "multiply":
                print("Result: ", multiply(num1, num2))
            elif user_input == "divide":
                print("Result: ", divide(num1, num2))
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()