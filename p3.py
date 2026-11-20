try:
    a = int(input())
    b = int(input())
    result = a / b
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Program completed")