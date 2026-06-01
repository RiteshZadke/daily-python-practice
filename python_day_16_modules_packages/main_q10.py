import student_input_q10
import calculations_q10
import report_q10
import storage_q10

name, marks = student_input_q10.get_student()

total = calculations_q10.total_marks(marks)
average = calculations_q10.average_marks(marks)

report_q10.generate_report(name, total, average)

storage_q10.save_report(name, total, average)