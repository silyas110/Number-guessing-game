# Simple Calculator
print("🧮 Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
operation = input("Operation: ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"Result: {result}")
