import file_utils_q8

file_utils_q8.write_file("sample.txt", "Hello\n")
file_utils_q8.append_file("sample.txt", "Welcome")

print(file_utils_q8.read_file("sample.txt"))