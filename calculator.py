def get_number(prompt):
    """Safely gets a float number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate(operation, num1, num2):
    """Performs the selected mathematical operation."""
    operations = {
        '1': ("Addition", num1 + num2),
        '2': ("Subtraction", num1 - num2),
        '3': ("Multiplication", num1 * num2),
        '4': ("Division", "Error: Division by zero is not allowed." if num2 == 0 else num1 / num2),
    }
    return operations.get(operation, ("Invalid", None))

def main():
    """Simple calculator with basic operations."""
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        operation = input("Enter the operation number (1-5): ")

        if operation == '5':
            print("Exiting calculator. Goodbye!")
            break

        if operation not in {'1', '2', '3', '4'}:
            print("Invalid selection. Please enter a number between 1 and 5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operation_name, result = calculate(operation, num1, num2)

        if result == "Error: Division by zero is not allowed.":
            print(result)
        else:
            print(f"{operation_name} result: {result}")

if __name__ == "__main__":
    main()