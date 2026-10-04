def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    if op == "add":
        print("Answer:", add(num1, num2))
    elif op == "subtract":
        print("Answer:", subtract(num1, num2))
    elif op == "multiply":
        print("Answer:", multiply(num1, num2))
    elif op == "divide":
        print("Answer:", divide(num1, num2))
    else:
        print("Invalid operation.")
except ValueError:
    print("Invalid input. Please enter numbers only.")