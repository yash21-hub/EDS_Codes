def calculate_grade(num_courses, marks):
    if len(marks) != num_courses:
        return "Error: Number of marks does not match number of courses."

    if any(mark < 40 for mark in marks):
        return "Fail"

    aggregate_percentage = sum(marks) / num_courses

    if aggregate_percentage > 75:
        grade = "Distinction"
    elif aggregate_percentage >= 60:
        grade = "First Division"
    elif aggregate_percentage >= 50:
        grade = "Second Division"
    elif aggregate_percentage >= 40:
        grade = "Third Division"
    else:
        grade = "Fail"

    return f"Aggregate Percentage: {aggregate_percentage:.2f}\nGrade: {grade}"


try:
    num_courses = int(input().strip())
    marks = list(map(int, input().strip().split()))

    result = calculate_grade(num_courses, marks)
    print(result)

except ValueError:
    print("Error: Invalid input. Please enter integers only.")