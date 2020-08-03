def grading_students(grades):
    rounded_grades = []
    for grade in grades:
        result_grade = grade
        rounded_grade = next_multiple_five(grade)
        if rounded_grade >= 40:
            result_grade = rounded_grade
        rounded_grades.append(result_grade)
    return rounded_grades


def next_multiple_five(num):
    if (num + 2) % 5 == 0:
        return num + 2
    elif (num + 1) % 5 == 0:
        return num + 1
    return num


def display(grades):
    for grade in grades:
        print(grade)


enter = [73, 67, 38, 33]
output = [75, 67, 40, 33]

display(grading_students(enter))

