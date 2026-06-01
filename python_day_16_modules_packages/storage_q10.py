def save_report(name, total, average):
    with open("students.txt", "a") as file:
        file.write(f"{name},{total},{average}\n")