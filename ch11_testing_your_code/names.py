from name_function import get_formatted_name as gtn

print("Enter 'q' to quit the program")

while True:
    first_name = input("Enter your first name: ")
    if first_name == 'q':
        break
    last_name = input("Enter your surname: ")
    if last_name == 'q':
        break

    formatted_name = gtn(first_name, last_name)
    print(f"\tNeatly formatted name: {formatted_name}")
