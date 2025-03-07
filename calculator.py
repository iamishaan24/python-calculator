"""Calculator module for performing basic arithmetic operations."""
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

calc = input("Enter the number of your choice: ")

cal_sum = float(num1) + float(num2)
sub = float(num1) - float(num2)
mul = float(num1) * float(num2)
div = float(num1) / float(num2)

if calc == '1':
    print("The sum of", num1, "and", num2, "is", cal_sum)
elif calc == '2':
    print("The difference of", num1, "and", num2, "is", sub)
elif calc == '3':
    print("The product of", num1, "and", num2, "is", mul)
elif calc == '4':
    print("The quotient of", num1, "and", num2, "is", div)
else:
    print("Invalid input")
    