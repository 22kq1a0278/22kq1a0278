try:
    a = int(input())
    b = int(input())
    result = a / b
except ValueError:
    print("Please enter valid integers")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division:", result)
finally:
    print("Program completed")