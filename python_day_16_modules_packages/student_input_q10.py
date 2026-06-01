def get_student():
    name = input("Enter Name: ")

    marks = []

    for i in range(5):
        marks.append(float(input(f"Enter Mark {i+1}: ")))

    return name, marks