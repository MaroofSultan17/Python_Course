
student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grade = {}
for key in student_score:
    if student_score[key] >= 81:
        student_grade[key] = "Excellent"
    elif 71 <= student_score[key] <= 80:
        student_grade[key] = "Acceptable"
    elif student_score[key] <= 70:
        student_grade[key] = "Fail"
for this in student_grade:
    print(this)
    print(student_grade[this])
# print(student_grade)