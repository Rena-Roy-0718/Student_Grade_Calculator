def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def main():
    print("===== Student Grade Calculator =====")

    name = input("Enter Student Name: ")

    num_subjects = int(input("Enter Number of Subjects: "))

    marks = []

    for i in range(num_subjects):
        mark = float(input(f"Enter Mark for Subject {i + 1}: "))
        marks.append(mark)

    average = calculate_average(marks)
    grade = assign_grade(average)

    print("\n===== RESULT =====")
    print("Student Name :", name)
    print("Average Marks:", round(average, 2))
    print("Grade        :", grade)

    if average >= 50:
        print("Status       : PASS")
    else:
        print("Status       : FAIL")


main()