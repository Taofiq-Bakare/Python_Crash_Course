"""
A simple program that reads text file

"""
filename = 'ch10_files_and_exceptions\pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         # contents = file_object.read()
#         print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
