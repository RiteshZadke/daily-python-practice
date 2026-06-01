employees = []

def add_employee(name):
    employees.append(name)

def search_employee(name):
    return name in employees

def display_employees():
    for employee in employees:
        print(employee) 