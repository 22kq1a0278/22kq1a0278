def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
a = int(input())
b = int(input())
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Result:", addition(a, b))
elif op == "-":
    print("Result:", subtraction(a, b))

elif op == "*":
    print("Result:", multiplication(a, b))
elif op == "/":
    try:
        print("Result:", division(a, b))
    except ZeroDivisionError:
        print("Cannot divide by zero")
else:
    print("Invalid operator")