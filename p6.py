def calculate_result(marks):
    total = 0
    for m in marks:
        total = total + m
    average = total / 5
    percentage = (total / 500) * 100
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print("Total:", total)
    print("Average:", average)
    print("Percentage:", percentage)
    print("Grade:", grade)


marks = []
i = 0

while i < 5:
    marks.append(int(input("Enter marks: ")))
    i = i + 1

calculate_result(marks)