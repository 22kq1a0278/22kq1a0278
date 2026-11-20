def second_largest(numbers):
    largest = numbers[0]
    second = None
    for i in numbers:
        if i > largest:
            second = largest
            largest = i

        elif i < largest:
            if second == None or i > second:
                second = i
    return second
numbers = [10, 20, 5, 30, 20, 30]
print("Second largest:", second_largest(numbers))