import student_utils_q6

marks = []

for i in range(5):
    marks.append(float(input(f'Enter mark {i+1}: ')))

total = student_utils_q6.calculate_total(marks)
average = student_utils_q6.calculate_average(marks)
grade = student_utils_q6.assign_grade(average)

print('Total:',total)
print('Average:',average)
print('Grade:',grade)