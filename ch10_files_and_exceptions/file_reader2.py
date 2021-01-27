"""
A simple text reader

"""


def reader(path):
    """
    A function that reads a text file
    and prints its contents with list
    """
    with open(path) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.replace('Python', 'Java').rstrip())


def write_name(file, name):
    """
    A simple function that write
    names to file
    """
    with open(file_name, 'a') as file_object:
        file_object.write(guest_name.title())
        file_object.write("\n")


def is_string_only(check_input):
    if check_input.isalpha():
        return True
    return False


# reader(file_path)

# to write to file
file_name = 'guest.txt'
file_path = "ch10_files_and_exceptions\exercise.txt"

count = 0
while True:
    count += 1
    guest_name = input("Enter your name: ")
    print(f"Your name is {guest_name.title()}")
    write_name(file_name, guest_name)
    if count == 3:
        break
