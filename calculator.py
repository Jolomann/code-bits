# First we need two numbers for calculation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# Then set the operation
operation = input("Enter operation (+, -, *, /): ")


# Ok now for calculation
if operation == "+":
	result = num1 + num2
elif operation == "-":
	result = num1 - num2
elif operation == "*":
	result = num1 * num2
elif operation == "/":
	result = num1 / num2
else:
	print("Something broke")

print(f"{result}")