try:
    numbers = input().split()
    index = int(input())
    print("Element:", numbers[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Please enter a valid index")